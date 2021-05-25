from flask import render_template, jsonify, request, make_response, redirect
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db, socket, valid_apikeys #limiter
from app.models import User
from app.workers import genarate_APIkey, hassu, get_all_users, get_admin_data, get_admins


@app.route('/')
@app.route('/index')
#@limiter.limit('1/10second')
def index():

    if current_user.is_authenticated and current_user.is_superuser:
        resp = make_response(render_template('auth.html', users=get_all_users(), data=get_admin_data(), admins=get_admins() ))
        resp.set_cookie('APIKEY', current_user.APIkey)
        return resp
    if current_user.is_authenticated and not current_user.is_superuser:
        resp = make_response(render_template('user.html'))
        resp.set_cookie('APIKEY', current_user.APIkey)
        return resp

    return render_template('base.html')


@app.route('/login', methods = ['POST'])
def login():
    if len(request.form) == 2:
        rem = False
    elif len(request.form) == 3:
        rem = True

    username = request.form['lusername']
    password = request.form['lpassword']

    for user in User.query.all():
        if user.username == str(username) and user.check_password(password):
            login_user(user, remember=rem)
            return redirect('/')

    # SHOW "no user or bad password" ERROR MESSAGE!!!!
    # socket send error
    return '', 204


@app.route('/logout', methods = ['GET'])
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('APIKEY')
    logout_user()
    return resp


@app.route('/register', methods = ['POST'])
def adduser():
    username = str(request.form.get('username'))
    password1 = str(request.form.get('password'))
    password2 = str(request.form.get('password2'))
    userlist = []
    for user in User.query.all():
        userlist.append(str(user.username))
    #implement checks!
    if password1 != password2 or username in userlist:
        #THROW ERROR! DO NOT REDIRECT!
        return('/')

    u = User()
    u.username = username
    u.is_superuser = False
    u.set_password(password1)
    u.APIkey = genarate_APIkey()
    db.session.add(u)
    db.session.commit()
    valid_apikeys.append(u.APIkey)
    login_user(u)
    return redirect('/')


@app.route('/addsu/<suname>/<password>')
def addsu(suname, password):
    if not hassu():

        user = User()
        user.username = suname
        user.set_password(password)
        user.is_superuser = True
        user.setkey(genarate_APIkey())
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        key = user.APIkey
        valid_apikeys.append(user.APIkey)

    return redirect('/')


@app.route('/deluser/<userid>', methods=['GET'])
@login_required
def del_user(userid):
    user = User.query.get(int(userid))
    if not user:
        #Respond with error!
        return 1
    else:
        db.session.delete(user)
        db.session.commit()

        return 0


@socket.on('admin')
def new_admin_message(data):

    if not current_user.is_authenticated or not current_user.is_superuser:
        return False

    # where to send the answer -> sid
    sid = request.sid

    # delete user with ID
    if data['event'] == 2201:
        return True
import json

#from app import db, login, fernet, logger
from app import db, login
import bcrypt
from datetime import datetime
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


'''
===============================
USERS
-------------------------------
 - id (int, u)
 - username (str/32/, u)
 - password_hash (str/128/)
 - salt (str/128/)
 - APIkey (str/64/)
 - created (date)
 - last_modified (date)
 - is_superuser (bool)
 - exercises 
===============================
'''

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password_hash = db.Column(db.String(128), default='')
    salt = db.Column(db.String(128), default='')
    APIkey = db.Column(db.String(64), index=True, default='')
    created = db.Column(db.Date(), default=datetime.now())
    last_modified = db.Column(db.Date(), default=datetime.now())
    is_superuser = db.Column(db.Boolean, default=False)

    exercises = db.relationship('Exercise', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<Username: {self.username}>'

    def set_password(self, password):
        salt = bcrypt.gensalt(14)
        p_bytes = password.encode()
        pw_hash = bcrypt.hashpw(p_bytes, salt)
        self.password_hash = pw_hash.decode()
        self.salt = salt.decode()
        return True

    def check_password(self, password):
        c_password = bcrypt.hashpw(password.encode(), self.salt.encode()).decode()
        if c_password == self.password_hash:
            return True
        else:
            return False

    def setkey(self, key):
        self.APIkey = key



'''
===============================
EXERCISES
-------------------------------
 - id (int, u)
 - name (str/32/)
 - description (str/128/, def=NO DESCRIPTION)
 - link (str/128/, def=NO VIDEO LINK)
 - user_id (FK -> User.id)
===============================
'''
class Exercise(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)
    name = db.Column(db.String(32), index=True)
    description = db.Column(db.String(128), default='Nincs leírás...')
    link = db.Column(db.String(128), default='Nics videó csatolva...')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Exercise name: {self.name} , ID: {self.id}>'
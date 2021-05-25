from random import SystemRandom
import app
from app import db
from app.models import User, Exercise, Competitor



def hassu():
    for user in User.query.all():
        if user.is_superuser: return True
    return False


def generate_rnd(N):
    import string
    return ''.join(SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N))


def genarate_APIkey():

    keys = []
    for user in User.query.all():
        keys.append(user.APIkey)

    key = generate_rnd(64)

    while key in keys:
        key = generate_rnd(64)

    return key


def get_all_users():
    return User.query.all()


def get_admin_data():
    '''
    [
        {
            id: id,
            username: username,
            apikey: APIkey,
            created: created,
            last_modified: last_ modified,
            is_superuser: is_superuser,
            exercises: [
                {
                    id: id,
                    name: name,
                    description: description;
                    link: link
                }
            ],
            competitors: [
                {
                    id: id,
                    name: name,
                    description: description,
                    weight: weight
                }
            ]
        }
    ]
    :return:
    '''

    data = []

    for user in User.query.filter_by(is_superuser=False):
        #init and zeroize dict elements
        u = {}
        es = []
        cs = []

        #iter over users and append k-v pairs
        u['id'] = user.id
        u['username'] = user.username
        u['apikey'] = user.APIkey
        u['created'] = user.created
        u['last_modified'] = user.last_modified
        u['is_superuser'] = user.is_superuser

        #iter over the exercises and append k-v pairs
        for exercise in Exercise.query.filter_by(user_id=user.id):
            e = {}
            e['id'] = exercise.id
            e['name'] = exercise.name
            e['description'] = exercise.description
            e['link'] = exercise.link
            es.append(e)

        #add all exercises of current user to dict
        u['exercises'] = es

        #iter over the competitors and append k-v pairs
        for competitor in Competitor.query.filter_by(user_id=user.id):
            c = {}
            c['id'] = competitor.id
            c['name'] = competitor.name
            c['description'] = competitor.description
            c['weight'] = competitor.weight
            cs.append(c)

        #add all competitors of current user to dict
        u['competitors'] = cs

        #add all data according to the current user to the list to return
        data.append(u)

        #print(f'data: {data}')

    return data


def get_admins():
    admins = []
    for user in User.query.filter_by(is_superuser=True):
        admins.append(user)

    return admins
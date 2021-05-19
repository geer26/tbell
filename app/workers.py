from random import SystemRandom
import app
from app import db
from app.models import User



def hassu():
    pass


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
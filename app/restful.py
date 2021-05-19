from flask_restful import Resource, reqparse, request

import app.workers
from app import api, valid_apikeys
from app.models import User
from flask import make_response

try:
    for user in User.query.all():
        valid_apikeys.append(user.APIkey)
except:
    pass


class HelloWorld(Resource):
    def get(self):
        if request.cookies.get('APIKEY') not in valid_apikeys:
            return 'HIBA', 404
        resp = make_response({'hello':'world!'})
        return resp

api.add_resource(HelloWorld, '/api')
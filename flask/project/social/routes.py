from flask_restful import Api, fields, marshal_with, reqparse, Resource
from flask import Blueprint, current_app, request, make_response, Response, g
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
print(os.path.join(os.path.dirname(__file__), "../"))
from database.users import Person
from infi.clickhouse_orm.database import Database


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(CURRENT_DIR,'..', 'config')

users = Blueprint('users', __name__, url_prefix='/users')
visit = Blueprint('visit', __name__, url_prefix='/visit')
location = Blueprint('location', __name__, url_prefix='/location')

database = Database('demo')


class Users(Resource):

    def post(self):
        # req = request.get_data().decode()
        # response = '123'
        return {'hello': 'users'}

    def get(self):

        total = Person.objects_in(database).count()
        return {'hello': 'users'}


class Visit(Resource):
    def post(self):
        # req = request.get_data().decode()
        # response = '123'
        # return Response(str(response), response.http_status,
        #                 mimetype='application/json')
        return {'hello': 'visit'}

    def get(self):
        total = Person.objects_in(database).count()
        return {'hello': total}


class Location(Resource):
    def post(self):
        # req = request.get_data().decode()
        # response = '123'
        # return Response(str(response), response.http_status,
        #                 mimetype='application/json')
        return {'hello': 'location'}

    def get(self):
        return {'hello': 'location'}


api = Api(users)
api.add_resource(Users, "")

api = Api(visit)
api.add_resource(Visit, "")

api = Api(location)
api.add_resource(Location, "")
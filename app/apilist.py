"""
this is api-list
"""
from app.app import app
from flask_restful import Api
from flask import Blueprint
from app.apis.v1.logintoken import Login
from app.apis.v1.user import UserAdd, EditUser, DelUser, SelectUser
from app.config.apipath import *

v1 = Blueprint('v1', __name__)
api = Api(v1)

api.add_resource(UserAdd, Userapi.add)
api.add_resource(EditUser, Userapi.edit)
api.add_resource(DelUser, Userapi.delete)
api.add_resource(SelectUser, Userapi.select)
api.add_resource(Login, LoginApi.login)
app.register_blueprint(v1, url_prefix='/v1')

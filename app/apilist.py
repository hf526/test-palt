"""
this is api-list
"""
from app.app import app
from flask_restful import Api
from flask import Blueprint
from app.apis.v1.logintoken import Login
from app.apis.v1.user import UserAdd, EditUser, DelUser, SelectUser

v1 = Blueprint('v1', __name__)
api = Api(v1)

api.add_resource(UserAdd, '/user/add')
api.add_resource(EditUser, '/user/edit')
api.add_resource(DelUser, '/user/del')
api.add_resource(SelectUser, '/user/select')
api.add_resource(Login, '/login')
app.register_blueprint(v1, url_prefix='/v1')

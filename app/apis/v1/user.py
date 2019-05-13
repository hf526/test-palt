"""
新增/编辑/删除/查询用户接口
"""
from flask_restful import Resource
from app.models import User
from app.forms.userforms import *
from app.config.status_code import *


class UserAdd(Resource):
    def post(self):
        request_data = UserAddData()
        username = User.query.filter_by(username=request_data[Verifyfromdata.username]).first()
        if username:
            return UserExist
        if User.add_update(User(**request_data)):
            return Success
        return UnknowError


class EditUser(Resource):
    def post(self):
        request_data = UserEdit()
        username = User.query.filter_by(username=request_data[Verifyfromdata.username]).first()
        if username:
            User.query.filter_by(username=Verifyfromdata.username).update(**request_data)
            User.add_update(User(**request_data))
            return Success
        return UserNull


class DelUser(Resource):
    def post(self):
        request_data = UserDel()
        user = User.query.filter_by(username=request_data[Verifyfromdata.id]).first()
        if User.delete_data(user):
            return Success
        return UserNull


class SelectUser(Resource):
    def get(self):
        request_data = UserSel()
        user = User.query.filter_by(username=request_data[Verifyfromdata.id]).first()
        if User.delete_data(user):
            return Success
        return UserNull

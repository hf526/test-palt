"""
新增/编辑/删除/查询用户接口
"""
from flask_restful import Resource
from app.models.model import User
from app.forms.userforms import *
from app.config.status_code import *
from app.libs.token import Verify


class UserAdd(Resource):
    @Verify
    def post(self):
        request_data = UserAddData()
        print('测试',request_data)
        username = User.query.filter_by(username=request_data.username).first()
        if username:
            return UserExist
        if User.add_update(request_data):
            return Success
        return UnknowError


class EditUser(Resource):
    @Verify
    def post(self):
        request_data = UserEdit()
        username = User.query.filter_by(username=request_data.username).first()
        if username:
            User.query.filter_by(username=request_data.username)
            User.add_update(request_data)
            return Success
        return UserNull


class DelUser(Resource):
    @Verify
    def post(self):
        request_data = UserDel()
        user = User.query.filter_by(username=request_data.id).first()
        if User.delete_data(user):
            return Success
        return UserNull


class SelectUser(Resource):
    @Verify
    def get(self):
        request_data = UserSel()
        schema = UserSchema()
        result = schema.load(request_data)
        print('请求参数',result)
        user = User.query.filter_by(username=request_data.id).first()
        if user:
            return '6666'
        return UserNull

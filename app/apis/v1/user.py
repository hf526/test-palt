"""
新增/编辑/删除/查询用户接口
"""
from flask_restful import Resource
from app.models.model import User
from app.forms.userforms import *
from app.config.status_code import *
from app.libs.token import Verify
from app.models.SerializeModel import UserSchema


class UserAdd(Resource):
    @Verify
    def post(self):
        request_data = UserAddData()
        username = User.query.filter_by(username=request_data.username).first()
        if username:
            return UserExist
        if User.add_update(request_data):
            return Success
        else:
            return ERR


class EditUser(Resource):
    @Verify
    def post(self):
        request_data = UserEdit()
        username = User.query.filter_by(id=request_data.id).first()
        if username:
            if User.add_update(**request_data):
                return Success
            else:
                return ERR
        return UserNull


class DelUser(Resource):
    @Verify
    def post(self):
        request_data = UserDel()
        user = User.query.filter_by(id=request_data.id).first()
        if user:
            if User.delete_data(user):
                return Success
            else:
                return ERR
        return UserNull


class SelectUser(Resource):
    @Verify
    def get(self):
        request_data = UserSel()
        user = User.query.filter_by(id=request_data.id).limit(request_data.limit).offset(request_data.page - 1)
        if user:
            schema = UserSchema(many=True)
            result = schema.dump(user).data
            result = {"data": result, "count": len(result)}
            return result
        return UserNull

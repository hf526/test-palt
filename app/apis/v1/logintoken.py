from flask_restful import Resource
from app.models import User
from app.forms.tokenfrom import *
from app.config.status_code import *
from flask import jsonify
from app.libs.token import create_auto_token


class GetToken(Resource):
    def post(self):
        request_data = get_login()
        username = User.query.filter_by(username=request_data[Loginfrom.username]).first()
        if username:
            password = request_data[Loginfrom.password]
            if User.check_pwd(username, password):
                token = create_auto_token(username.username, username.role)
                return jsonify({"token": token})
        return UserNull


class Login(Resource):
    def post(self):
        request_data = get_login()
        username = User.query.filter_by(username=request_data[Loginfrom.username]).first()
        if username:
            password = request_data[Loginfrom.password]
            if User.check_pwd(username, password):
                return LoginSuccess
        return UserNull

"""
create by ---追光者。
"""
from flask_restful import Resource
from app.models.model import User
from app.forms.tokenfrom import *
from app.config.status_code import *
from app.libs.common import Res
from app.libs.token import create_auto_token


class Login(Resource):
    def post(self):
        request_data = get_login()
        username = User.query.filter_by(username=request_data[Loginfrom.username]).first()
        if username:
            password = request_data[Loginfrom.password]
            if User.check_pwd(username, password):
                token = create_auto_token(username=request_data.username, role=username.role)
                return Res(LoginSuccess, token=token)
            else:
                return PasswordErr
        return UserNull

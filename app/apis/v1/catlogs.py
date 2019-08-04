"""
create by ---追光者。
"""
from flask_restful import Resource
from app.config.status_code import *
from app.libs.common import Res
from app.libs.token import create_auto_token


class Login(Resource):
    def post(self):
        pass

"""
token认证序列化
"""
from flask_restful import reqparse


class Loginfrom:
    """
    登陆用的参数主类
    """
    username = 'username'
    password = 'password'
    client = 'client'
    role = "role"


def get_login():
    parser = reqparse.RequestParser()
    parser.add_argument(Loginfrom.username, type=str, required=True)
    parser.add_argument(Loginfrom.password, type=str, required=True)
    parser.add_argument(Loginfrom.client, type=int)
    args = parser.parse_args()
    return args

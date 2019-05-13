"""
首先主类定义前端需要传递的字段，定义函数获取前端参数，序列化成字典返回
"""
from flask_restful import reqparse


class Verifyfromdata:
    """
    对于用户操作需要用到的字段类
    """
    id = 'id'
    name = 'name'
    username = 'username'
    role = 'role'
    client = 'client'
    password = 'password'
    limit = 'limit'
    page = 'page'


def UserAddData():
    """
    新增用户获取前端参数返回字典
    """
    parser = reqparse.RequestParser()
    parser.add_argument(Verifyfromdata.name, type=str, required=True)
    parser.add_argument(Verifyfromdata.username, type=str, required=True)
    parser.add_argument(Verifyfromdata.password, type=str, required=True)
    parser.add_argument(Verifyfromdata.role, type=int)
    args = parser.parse_args()
    return args


def UserEdit():
    """
    编辑用户获取前端参数返回字典
    """
    parser = reqparse.RequestParser()
    parser.add_argument(Verifyfromdata.name, type=str)
    parser.add_argument(Verifyfromdata.password, type=str)
    parser.add_argument(Verifyfromdata.role, type=int)
    args = parser.parse_args()
    return args


def UserSel():
    """
    查询用户获取前端参数返回字典
    """
    parser = reqparse.RequestParser()
    parser.add_argument(Verifyfromdata.id, type=int)
    parser.add_argument(Verifyfromdata.limit, type=int)
    parser.add_argument(Verifyfromdata.page, type=int)
    parser.add_argument(Verifyfromdata.name, type=str)
    parser.add_argument(Verifyfromdata.username, type=str)
    parser.add_argument(Verifyfromdata.role, type=int)
    args = parser.parse_args()
    return args


def UserDel():
    """
    删除用户传递的字段
    """
    parser = reqparse.RequestParser()
    parser.add_argument(Verifyfromdata.id, type=int, required=True)
    args = parser.parse_args()
    return args


class ToClass:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def todict(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

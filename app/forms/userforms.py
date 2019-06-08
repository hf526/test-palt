"""
首先主类定义前端需要传递的字段，定义函数获取前端参数，序列化成字典返回
"""
from flask_restful import reqparse
from app.models.SerializeModel import UserSchema


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
    create_time = 'create_time'
    update_time = 'update_time'


def UserAddData():
    """
    获取前端参数返回字典,
    然后序列化进行前端序列化成对象返回
    """
    parser = reqparse.RequestParser()
    parser.add_argument(Verifyfromdata.name, type=str, required=True)
    parser.add_argument(Verifyfromdata.username, type=str, required=True)
    parser.add_argument(Verifyfromdata.password, type=str, required=True)
    parser.add_argument(Verifyfromdata.role, type=str, required=True)
    args = parser.parse_args()
    role = args.get(Verifyfromdata.role)
    schema = UserSchema()
    args = schema.load(args).data
    print(args)
    return args, role


def UserEdit():
    """
    获取前端参数返回字典,
    然后序列化进行前端序列化成对象返回
    """
    parser = reqparse.RequestParser()
    parser.add_argument(Verifyfromdata.id, type=str, required=True)
    parser.add_argument(Verifyfromdata.name, type=str)
    parser.add_argument(Verifyfromdata.password, type=str)
    parser.add_argument(Verifyfromdata.role, type=int)
    args = parser.parse_args()
    schema = UserSchema()
    args = schema.load(args).data
    return args


def UserSel():
    """
    获取前端参数返回字典,
    然后序列化进行前端序列化成对象返回
    """
    parser = reqparse.RequestParser()
    parser.add_argument(Verifyfromdata.id, type=int)
    parser.add_argument(Verifyfromdata.limit, type=int)
    parser.add_argument(Verifyfromdata.page, type=int)
    parser.add_argument(Verifyfromdata.name, type=str)
    parser.add_argument(Verifyfromdata.username, type=str)
    parser.add_argument(Verifyfromdata.create_time, type=str)
    parser.add_argument(Verifyfromdata.update_time, type=str)
    args = parser.parse_args()
    schema = UserSchema()
    args = schema.load(args).data
    return args


def UserDel():
    """
    获取前端参数返回字典,
    然后序列化进行前端序列化成对象返回
    """
    parser = reqparse.RequestParser()
    parser.add_argument(Verifyfromdata.id, type=int, required=True)
    args = parser.parse_args()
    schema = UserSchema()
    args = schema.load(args).data
    return args


class ToClass:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def todict(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

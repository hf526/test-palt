"""
生成token的方法,用户名+权限+当前时间
并且验证token传递name合法性
"""
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
import time
from app.config.status_code import *
from app.config.config import SECRET_KEY
from collections import namedtuple
from flask import g, request


def create_auto_token(username, role, nowtime=time.time()):
    """
    生成token的方法
    :param username: 用户名
    :param role: 角色权限
    :param nowtime: 权限认证的时间
    :return:
    """
    expiration = int(time.time()) + 7200 - int(nowtime)
    s = Serializer(SECRET_KEY, expires_in=expiration)
    token = s.dumps(dict(username=username, role=role))
    return str(token, 'utf-8')


def Verifytoken():
    try:
        token = request.headers["token"]
        s = Serializer(SECRET_KEY, expires_in=7200)
        try:
            data = s.loads(token)
        except BadSignature:
            return TokenInvaild
        except SignatureExpired:
            return TokenExpired
        username = data['username']
        role = data['role']
        User = namedtuple('Token', ['username', 'role'])
        return User(username=username, role=role)
    except KeyError:
        return NotLogin


def Verify(func):
    def wrapper(*args, **kwargs):
        userinfo = Verifytoken()
        if "username" in userinfo:
            print(1)
            func(*args, **kwargs)
        else:
            return userinfo
    return wrapper

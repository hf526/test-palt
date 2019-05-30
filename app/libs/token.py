"""
生成token的方法,用户名+权限+当前时间
并且验证token传递name合法性
"""
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
import time
from app.config.status_code import *
from app.config.config import SECRET_KEY
from app.models.model import User
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
    """
    token验证函数
    :return:验证通过返回token包含的参数
    """
    try:
        token = request.headers["token"]
        s = Serializer(SECRET_KEY, expires_in=7200)
        try:
            data = s.loads(token)
        except BadSignature:
            return TokenInvaild
        except SignatureExpired:
            return TokenExpired
        user = User.query.filter_by(username=data.username).first()
        if user:
            return data
        return UserNull
    except KeyError:
        return NotLogin


def Verify(func):
    """
    验证token有效性的装饰器
    :param func: 函数
    :return: api函数
    """

    def wrapper(*args, **kwargs):
        userinfo = Verifytoken()
        if type(userinfo) == dict:
            try:
                return func(*args, **kwargs)
            except:
                return UnknowError
        else:
            return userinfo

    return wrapper

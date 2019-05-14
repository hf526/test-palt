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
from flask import g

def create_auto_token(username, Permission, nowtime=time.time()):
    expiration = int(time.time()) + 7200 - int(nowtime)
    s = Serializer(SECRET_KEY, expires_in=expiration)
    token = s.dumps(dict(username=username, Permission=Permission))
    return str(token, 'utf-8')


def Verifytoken(token):
    UserInfo = Gettokenmessage(token)
    if UserInfo:
        g.user = UserInfo
        print(g.user)
        return True
    else:
        return False


def Gettokenmessage(token):
    s = Serializer(SECRET_KEY, expires_in=7200)
    try:
        data = s.loads(token)
    except BadSignature:
        return TokenInvaild
    except SignatureExpired:
        return TokenExpired
    username = data['username']
    Permission = data['Permission']
    User = namedtuple('Token', ['username', 'Permission'])
    return User(username='username', Permission='Permission')

create_auto_token("测试",'1')
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
import time
from app.config.status_code import *
from app.config.config import SECRET_KEY

"""
生成token，用户名+权限+当前时间
"""

"""生成token的方法"""


def create_auto_token(username, Permission, nowtime=time.time()):
    expiration = int(time.time()) + 7200 - int(nowtime)
    s = Serializer(SECRET_KEY, expires_in=expiration)
    token = s.dumps(dict(username=username, Permission=Permission))
    return str(token, 'utf-8')


"""token装饰器"""


def Verifytoken(token):
    s = Serializer(SECRET_KEY, expires_in=7200)
    try:
        data = s.loads(token)
    except BadSignature:
        return TokenInvaild
    except SignatureExpired:
        return TokenExpired
    username = data['username']
    Permission = data['Permission']


create_auto_token(1, 1)

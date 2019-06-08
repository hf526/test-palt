"""
状态码：
成功一律返回0
token 登陆验证类一律返回  1
外部错误码一律返回  1XXXX
权限类一律  2XXXX
未知错误一律 -1
"""
UnknowError = dict(
    code=-1,
    msg="未知错误"
)
Success = dict(
    code=0,
    data="操作成功"
)
ERR = dict(
    code=0,
    data="操作失败"
)
LoginSuccess = dict(
    code=0,
    data="登陆成功"
)
TokenInvaild = dict(
    code=1,
    msg="token is invaild"
)
TokenExpired = dict(
    code=1,
    msg="token is expired"
)
NotLogin = dict(
    code=1001,
    data="请先登录"
)
UserNull = dict(
    code=1002,
    msg="用户不存在"
)
PasswordErr = dict(
    code=1003,
    msg="密码错误"
)
UserExist = dict(
    code=1004,
    msg="用户已存在"
)
NOPERMISSION = dict(
    code=2001,
    msg="无访问权限/权限等级不够"
)

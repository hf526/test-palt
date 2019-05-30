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
NotLogin = dict(
    code=1000,
    data="请先登录"
)
UserNull = dict(
    code=1001,
    msg="用户不存在"
)
PasswordErr = dict(
    code=1001,
    msg="密码错误"
)
TokenInvaild = dict(
    code=1,
    msg="token is invaild"
)
TokenExpired = dict(
    code=1,
    msg="token is expired"
)
UserExist = dict(
    code=1002,
    msg="用户已存在"
)
UnknowError = dict(
    code=1003,
    msg="未知错误"
)

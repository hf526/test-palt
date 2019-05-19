def StatusCode(**kwargs):
    return kwargs


Success = StatusCode(
    code=0,
    data="操作成功"
)
LoginSuccess = StatusCode(
    code=0,
    data="登陆成功"
)
UserNull = StatusCode(
    code=1001,
    msg="用户不存在"
)
PasswordErr = StatusCode(
    code=1001,
    msg="用户不存在"
)
TokenInvaild = StatusCode(
    code=1,
    msg="token is invaild"
)
TokenExpired = StatusCode(
    code=1,
    msg="token is expired"
)
UserExist = StatusCode(
    code=1002,
    msg="用户已存在"
)
UnknowError = StatusCode(
    code=1003,
    msg="操作失败"
)

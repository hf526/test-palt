"""
create by ---追光者。
webscoket:https://www.jianshu.com/p/fe5f19df1e77
"""
from flask_restful import Resource
# from app.config.status_code import *
from app.libs.common import Res
import paramiko
from app.config.linux_config import LinuxConfig

# from app.libs.token import create_auto_token

class CoonectLinux:
    def coonect_aly(self, hostname=LinuxConfig.ip, port=LinuxConfig.port, username=LinuxConfig.user,
                    password=LinuxConfig.password):
        # 实例化SSHClient
        client = paramiko.SSHClient()
        # 自动添加策略，保存服务器的主机名和密钥信息
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接SSH服务端，以用户名和密码进行认证
        client.connect(hostname, port=port, username=username, password=password, timeout=50)
        # 实例化Transport，并建立会话Session
        channel = client.get_transport().open_session()
        channel.get_pty()
        channel.exec_command('tail -F /root/test/test.log')
        while True:
            if channel.active:
                result = channel.recv(1024).decode()
                if len(result) != 0:
                    print(result)
                else:
                    print("测试")
                    break
        print("测试1")
        client.close()


class UserLogin(Resource):
    def post(self):
        return Res(data={"code": 20000, "data": {'token': "admin-token"}})


class UserInfo(Resource):
    def get(self):
        return Res(data={"code": 20000, "data": dict(roles=['admin'], introduction='I am a super administrator',
                                                     avatar='https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                                                     name='Super Admin')})


class GetLogs(Resource):
    def post(self):
        a = CoonectLinux()
        a.coonect_aly()
        return Res(data={"code": 20000, "data": dict(roles=['admin'], introduction='I am a super administrator',
                                                     avatar='https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
                                                     name='Super Admin')})


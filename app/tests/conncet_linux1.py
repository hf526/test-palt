"""
动态监控日志
参考：https://www.jb51.net/article/134134.htm
"""
import paramiko
from app.config.linux_config import LinuxConfig


class CoonectLinux:
    def coonect_aly(self, hostname=LinuxConfig.ip, port=LinuxConfig.port, username=LinuxConfig.user,
                    password=LinuxConfig.password):
        # 实例化SSHClient
        client = paramiko.SSHClient()
        # 自动添加策略，保存服务器的主机名和密钥信息
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接SSH服务端，以用户名和密码进行认证
        client.connect(hostname, port=port, username=username, password=password,timeout=50)
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
        # 执行命令

        # #接受日志信息
        # while True:
        #     recv = channel.recv(1024)
        #     print(recv.decode())


a = CoonectLinux()
a.coonect_aly()

"""
来源：https://www.cnblogs.com/zhangxinqi/p/8372774.html
"""
import paramiko
from app.config.linux_config import LinuxConfig


class CoonectLinux:
    def coonect_aly(self, hostname=LinuxConfig.ip, port=LinuxConfig.port, username=LinuxConfig.user,
                    password=LinuxConfig.password):
        # 创建sshclient对象
        ssh = paramiko.SSHClient()
        # 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 调用connect方法连接服务器
        ssh.connect(hostname=hostname, port=port, username=username, password=password)
        #执行命令
        stdin, stdout, stderr=ssh.exec_command('ll')
        print(stdout.read().decode())
        ssh.close()

a=CoonectLinux()
a.coonect_aly()
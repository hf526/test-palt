"""
来源：https://www.cnblogs.com/zhangxinqi/p/8372774.html
https://blog.csdn.net/weixin_39912556/article/details/80576624
https://www.cnblogs.com/xiao-apple36/p/9144092.html#_label1
http://www.mamicode.com/info-detail-2151386.html
http://www.maiziedu.com/wiki/frame/brief/
"""
import paramiko
import sys
import os
import select
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
        # 执行命令
        number = 0
        while True:
            stdin, stdout, stderr = ssh.exec_command('cat -n /root/test/test.log')
            print(stdout.read().decode())
            nownumber = stdout.read().decode().split('\n')
            print(nownumber)
            if number != nownumber:
                print('测试')
                print(stdout.read().decode())
                number = nownumber
            ssh.close()

    def connect_aly2(self, hostname=LinuxConfig.ip, port=LinuxConfig.port, username=LinuxConfig.user,
                     password=LinuxConfig.password):
        # 实例化一个transport对象
        trans = paramiko.Transport((hostname, port))
        # 建立连接
        trans.connect(username=username, password=password)

        # 将sshclient的对象的transport指定为以上的trans
        ssh = paramiko.SSHClient()
        ssh._transport = trans
        # 执行命令，和传统方法一样
        stdin, stdout, stderr = ssh.exec_command('tail -1000 /root/test/test.log')
        print(stdout.read().decode())

        # 关闭连接
        trans.close()

    def connect_aly3(self, hostname=LinuxConfig.ip, port=LinuxConfig.port, username=LinuxConfig.user,
                     password=LinuxConfig.password):
        """实现动态感知日志"""
        # 建立一个socket
        trans = paramiko.Transport((hostname, port))
        # 启动一个客户端
        trans.start_client()

        # 如果使用rsa密钥登录的话
        '''
        default_key_file = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
        prikey = paramiko.RSAKey.from_private_key_file(default_key_file)
        trans.auth_publickey(username='super', key=prikey)
        '''
        # 如果使用用户名和密码登录
        trans.auth_password(username=username, password=password)
        # 打开一个通道
        channel = trans.open_session()
        # 获取终端
        channel.get_pty()
        # 激活终端，这样就可以登录到终端了，就和我们用类似于xshell登录系统一样
        channel.invoke_shell()
        # 下面就可以执行你所有的操作，用select实现
        # 对输入终端sys.stdin和 通道进行监控,
        # 当用户在终端输入命令后，将命令交给channel通道，这个时候sys.stdin就发生变化，select就可以感知
        # channel的发送命令、获取结果过程其实就是一个socket的发送和接受信息的过程
        while True:
            readlist, writelist, errlist = select.select([channel, sys.stdin, ], [], [])
            # 如果是用户输入命令了,sys.stdin发生变化
            if sys.stdin in readlist:
                # 获取输入的内容
                input_cmd = sys.stdin.read(1)
                # 将命令发送给服务器
                channel.sendall(input_cmd)

            # 服务器返回了结果,channel通道接受到结果,发生变化 select感知到
            if channel in readlist:
                # 获取结果
                result = channel.recv(1024)
                # 断开连接后退出
                if len(result) == 0:
                    print("\r\n**** EOF **** \r\n")
                    break
                # 输出到屏幕
                sys.stdout.write(result.decode())
                sys.stdout.flush()

        # 关闭通道
        channel.close()
        # 关闭链接
        trans.close()


a = CoonectLinux()
a.coonect_aly()

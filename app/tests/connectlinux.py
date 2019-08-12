"""
来源：https://www.cnblogs.com/zhangxinqi/p/8372774.html
https://blog.csdn.net/weixin_39912556/article/details/80576624
https://www.cnblogs.com/xiao-apple36/p/9144092.html#_label1
http://www.mamicode.com/info-detail-2151386.html
http://www.maiziedu.com/wiki/frame/brief/
https://www.xuebuyuan.com/1107365.html
https://blog.csdn.net/diyiday/article/details/81871054
https://blog.csdn.net/s740556472/article/details/78991704
重点：http://www.169it.com/blog_article/3781956955.html
"""
import paramiko
import sys
import os
import select
from app.config.linux_config import LinuxConfig
from paramiko_expect import SSHClientInteraction


class CoonectLinux:
    def coonect_aly(self, hostname=LinuxConfig.ip, port=LinuxConfig.port, username=LinuxConfig.user,
                    password=LinuxConfig.password):
        # 进行连接
        print('------------开始连接服务器(%s)-----------' % hostname)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print('------------开始认证......-----------')
        client.connect(hostname, port, username=username, password=password, timeout=4)
        print('------------认证成功!.....-----------')
        # 开启channel 管道
        transport = client.get_transport()
        channel = transport.open_session()
        channel.get_pty()
        # 执行命令nohup.log.2017-12-30
        tail = 'tail -f /root/test/test.log'
        # 将命令传入管道中
        channel.exec_command(tail)
        # rl, wl, el = select.select([channel], [], [])
        while True:
            # 判断退出的准备状态
            if channel.exit_status_ready():
                break
            try:
                recv = channel.recv(1024)
                # 通过socket进行读取日志，个人理解，linux相当于客户端，我本地相当于服务端请求获取数据（此处若有理解错误，望请指出。。谢谢）
                # if len(rl) > 0:

                    # 此处将获取的数据解码成gbk的存入本地日志
                print(recv.decode('gbk', 'ignore'))
                print(111)
            # 键盘终端异常
            except KeyboardInterrupt:
                print("Caught control-C")
                channel.send("\x03")  # 发送 ctrl+c
                channel.close()
            print("测试")
        print("测试1")
        client.close()




a = CoonectLinux()
a.coonect_aly()

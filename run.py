"""
综合执行文件
init构建数据库
update更新数据库模型
back 回退上个版本
api 生成api文档
run 运行服务器
其他  重新输入
"""
import os


def inputc():
    system = input()
    os.system("pipenv shell")
    if system == "init":
        os.system("python manage.py db init")
        os.system("python manage.py db migrate")
        os.system("python manage.py db upgrade")
    elif system == "update":
        os.system("python manage.py db migrate")
        os.system("python manage.py db upgrade")
    elif system == "back":
        os.system("python manage.py db downgrade")
    elif system == "api":
        os.system("apidoc -i views/ -o static/apidoc")
    elif system == "run":
        os.system("python manage.py runserver")
    else:
        inputc()


if __name__ == '__main__':
    inputc()
    # app.run()

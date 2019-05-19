"""
导入flask实例，orm实例，迁移库，命令行管理库
实例化APP,配置数据库链接地址
实例化db对象
manager添加命令行实例
创建迁移脚本绑定app和db，添加命令(重点需在最后注册蓝图)
"""
from flask import Blueprint
from app.exts import app
from flask_restful import Api
from app.apis.v1.user import UserAdd, EditUser, DelUser, SelectUser
from app.apis.v1.logintoken import Login

app.config.from_object("app.config.config.Eev")

v1 = Blueprint('v1', __name__)
api = Api(v1)

api.add_resource(UserAdd, '/user/add')
api.add_resource(EditUser, '/user/edit')
api.add_resource(DelUser, '/user/del')
api.add_resource(SelectUser, '/user/select')
api.add_resource(Login, '/login')
app.register_blueprint(v1, url_prefix='/v1')

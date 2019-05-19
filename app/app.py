"""
导入app对象和蓝图对象
给对应的类注册相应的api地址
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

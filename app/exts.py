"""
导入flask实例，orm实例，迁移库，命令行管理库
实例化APP,配置数据库链接地址
实例化db对象
manager添加命令行实例
创建迁移脚本绑定app和db，添加命令
"""
"""
导入flask实例，orm实例，迁移库，命令行管理库
实例化APP,配置数据库链接地址
实例化db对象
manager添加命令行实例
创建迁移脚本绑定app和db，添加命令
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy(app)
ma = Marshmallow(app)

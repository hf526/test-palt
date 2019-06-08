"""
专门用来生成APP和db实例，避免循环导入问题
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# app.config["SQLALCHEMY_ECHO"] = True
app.config.from_object("app.config.config.Eev")
db = SQLAlchemy(app)
ma = Marshmallow(app)

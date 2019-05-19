"""
导入flask实例，orm实例，序列化实例
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow

app = Flask(__name__)
db = SQLAlchemy(app)
# ma = Marshmallow(app)

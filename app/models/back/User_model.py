from app.models.back.Base import db, Base
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(128), comment="用户昵称", default="未填写昵称用户")
    username = db.Column(db.String(128), unique=True, comment="用户名")
    pwd_hash = db.Column(db.String(512), comment="密码")
    role = db.Column(db.Integer, comment="用户角色")
    status = db.Column(db.Integer, comment="状态")

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.hspassword = password
        self.role = role

    # 读
    @property
    def hspassword(self):
        return ''

    # 写
    @hspassword.setter
    def hspassword(self, password):
        self.pwd_hash = generate_password_hash(password)

    # 对比
    def check_pwd(self, pwssword):
        return check_password_hash(self.pwd_hash, pwssword)

    def __repr__(self):
        return '<Project %r>' % self.__tablename__

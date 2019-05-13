from app.exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Base:
    create_time = db.Column(db.DateTime, default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), comment="创建时间")
    update_time = db.Column(db.DateTime, default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), comment="更新时间")

    def add_update(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e

    def delete_data(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return e


class User(Base, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(128), comment="用户昵称", default="未填写昵称用户")
    username = db.Column(db.String(128), unique=True, comment="用户名")
    pwd_hash = db.Column(db.String(512), comment="密码")
    role = db.Column(db.String(80), comment="用户角色")

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

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            username=self.username,
            role=self.role,
            create_time=self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            update_time=self.update_time.strftime('%Y-%m-%d %H:%M:%S')
        )

    def __repr__(self):
        return '<Project %r>' % self.__tablename__


class Project(Base, db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(80), unique=True, comment="项目名称")
    comment = db.Column(db.String(80), comment="项目描述")

    def to_dict(self):
        return dict(
            id=self.id,
            comment=self.comment,
        )

    def __repr__(self):
        return '<Project %r>' % self.__tablename__


class Case(Base, db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(80), comment="用例名称")
    comment = db.Column(db.String(512), comment="用例描述")
    expect = db.Column(db.String(512), comment="期望响应结果")
    response = db.Column(db.String(512), comment="实际响应结果")

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            comment=self.comment,
            expect=self.expect,
            response=self.response
        )

    def __repr__(self):
        return '<Case %r>' % self.__tablename__


class Api(Base, db.Model):
    __tablename__ = 'api'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    path = db.Column(db.String(80), comment="接口地址")
    header = db.Column(db.String(80), comment="请求头")
    method = db.Column(db.String(128), comment="请求方式")
    data = db.Column(db.String(512), comment="接口参数")

    def to_dict(self):
        return dict(
            id=self.id,
            path=self.path,
            header=self.header,
            method=self.method,
            data=self.data
        )

    def __repr__(self):
        return '<Api %r>' % self.__tablename__


class WebConfig(Base, db.Model):
    __tablename__ = 'webconfig'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(80), comment="配置名称")
    url = db.Column(db.String(80), comment="环境地址")
    header = db.Column(db.String(80), comment="公共请求头")

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            url=self.url,
            header=self.header,
        )

    def __repr__(self):
        return '<Api %r>' % self.__tablename__


class Logs(Base, db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    operation = db.Column(db.String(80), comment="操作描述")
    client = db.Column(db.Integer, comment="最后操作的客户端")

    def to_dict(self):
        return dict(
            id=self.id,
            operation=self.operation,
        )

    def __repr__(self):
        return '<Api %r>' % self.__tablename__


class Variable(Base, db.Model):
    __tablename__ = 'variable'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    variable_name = db.Column(db.String(80), comment="变量名称")
    script = db.Column(db.String(80), comment="脚本")

    def to_dict(self):
        return dict(
            id=self.id,
            variable_name=self.variable_name,
            script=self.script,
        )

    def __repr__(self):
        return '<Api %r>' % self.__tablename__

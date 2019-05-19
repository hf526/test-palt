from app.models.back.Base import db, Base


class Case(Base, db.Model):
    __tablename__ = 'case'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(80), comment="用例名称")
    comment = db.Column(db.String(512), comment="用例描述")
    expect = db.Column(db.String(512), comment="期望响应结果")
    response = db.Column(db.String(512), comment="实际响应结果")
    status = db.Column(db.Integer, comment="状态")

    def __repr__(self):
        return '<Case %r>' % self.__tablename__

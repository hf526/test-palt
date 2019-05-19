from app.models.back.Base import db, Base


class Api(Base, db.Model):
    __tablename__ = 'api'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    path = db.Column(db.String(80), comment="接口地址")
    header = db.Column(db.String(80), comment="请求头")
    method = db.Column(db.String(128), comment="请求方式")
    data = db.Column(db.String(512), comment="接口参数")
    status = db.Column(db.Integer, comment="状态")

    def __repr__(self):
        return '<Api %r>' % self.__tablename__

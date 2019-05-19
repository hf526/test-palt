from app.models.Base import db, Base


class WebConfig(Base, db.Model):
    __tablename__ = 'webconfig'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(80), comment="配置名称")
    url = db.Column(db.String(80), comment="环境地址")
    header = db.Column(db.String(80), comment="公共请求头")
    status = db.Column(db.Integer, comment="状态")

    def __repr__(self):
        return '<Api %r>' % self.__tablename__

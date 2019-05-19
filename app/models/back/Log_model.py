from app.models.back.Base import db, Base

class Logs(Base, db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    operation = db.Column(db.String(80), comment="操作描述")
    client = db.Column(db.Integer, comment="最后操作的客户端")

    def __repr__(self):
        return '<Api %r>' % self.__tablename__


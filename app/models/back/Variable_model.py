from app.models.back.Base import db, Base


class Variable(Base, db.Model):
    __tablename__ = 'variable'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    variable_name = db.Column(db.String(80), comment="变量名称")
    script = db.Column(db.String(80), comment="脚本")
    status = db.Column(db.Integer, comment="状态")

    def __repr__(self):
        return '<Api %r>' % self.__tablename__

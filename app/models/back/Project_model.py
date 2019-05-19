from app.models.back.Base import db, Base


class Project(Base, db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, comment="主键")
    name = db.Column(db.String(80), unique=True, comment="项目名称")
    comment = db.Column(db.String(80), comment="项目描述")
    status = db.Column(db.Integer, comment="状态")

    def __repr__(self):
        return '<Project %r>' % self.__tablename__

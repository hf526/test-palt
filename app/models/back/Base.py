from app.exts import db
from datetime import datetime

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

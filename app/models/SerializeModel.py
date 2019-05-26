"""
序列化model的类
"""
from app.app import ma
from app.models.model import User, Role, Case, Api, WebConfig, Logs, Variable


class UserSchema(ma.Schema):
    class Meta:
        model = User

#
# user = User.query.filter_by(username='test1').first()
# schema = UserSchema()
# result = schema.dump(user)
# result = schema.dump(result.data)
#
# print(result.data)

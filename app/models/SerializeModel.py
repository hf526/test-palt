"""
序列化model的类
"""
from marshmallow import Schema, fields, post_load
from app.models.model import User


class UserSchema(Schema):
    """用户序列化类"""
    id = fields.Integer()
    name = fields.Str()
    username = fields.Str()
    password = fields.Str()
    status = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()

    @post_load
    def make_user(self, data):
        return User(**data)

# from app.app import ma
# from app.models.model import User
#
#
# class UserSchema(ma.ModelSchema):
#     class Meta:
#         model = User
#
#     @post_load
#     def make_user(self, data):
#         return User(**data)

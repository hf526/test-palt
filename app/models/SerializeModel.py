"""
序列化model的类
"""
from marshmallow import Schema, fields, post_load


class UserSchema(Schema):
    """用户序列化类"""
    id = fields.Integer()
    name = fields.Str()
    username = fields.Str()
    status = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()

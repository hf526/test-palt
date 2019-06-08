"""
新增/编辑/删除/查询用户接口
"""
from flask_restful import Resource
from sqlalchemy import and_, or_
from app.models.model import User
from app.forms.userforms import *
from app.config.status_code import *
from app.libs.token import Verify, Verifypermission
from app.libs.common import Res



class UserAdd(Resource):
    @Verifypermission
    def post(self):
        data, role = UserAddData()
        username = User.query.filter_by(username=data.username).first()
        if username:
            return Res(UserExist)
        elif User.add_user(data, role):
            return Res(Success)
        else:
            return Res(ERR)


class EditUser(Resource):
    @Verifypermission
    @Verify
    def post(self):
        request_data = UserEdit()
        username = User.query.filter_by(id=request_data.id).first()
        if username:
            if User.add_update(request_data):
                return Res(Success)
            else:
                return Res(ERR)
        return Res(UserNull)


class DelUser(Resource):
    @Verifypermission
    @Verify
    def post(self):
        request_data = UserDel()
        user = User.query.filter_by(id=request_data.id).first()
        if user:
            if User.delete_data(user):
                return Res(Success)
            else:
                return Res(ERR)
        return Res(UserNull)


class SelectUser(Resource):
    @Verifypermission
    @Verify
    def post(self):
        """
        查询接口，默认查500条
        """
        data = UserSel()
        page = data.page - 1 if data.page else 0
        count = data.limit if data.limit else 500
        create_time = data.create_time if data.create_time is not None else ""
        update_time = data.update_time if data.update_time is not None else ""
        name = data.name if data.name is not None else ''
        """查询需要的结果"""
        user = User.query.filter(
            or_(User.id == data.id, User.name.like('%' + name + '%'), User.username == data.username),
            and_(User.create_time > create_time, User.update_time > update_time)).limit(count).offset(page)
        """查询得到总计数"""
        count = User.query.filter(
            or_(User.id == data.id, User.name.like('%' + name + '%'), User.username == data.username),
            and_(User.create_time > create_time, User.update_time > update_time)).count()
        if user:
            schema = UserSchema(many=True)
            result = schema.dump(user).data
            result = {"data": result, 'sumcounts': count, "count": user.count()}
            return Res(result)
        return Res(UserNull)

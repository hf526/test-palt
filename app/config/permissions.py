"""
create by --追光者
"""
from app.config.apipath import *

RolePermission_v1 = {
    Userapi.add: ['admin'],
    Userapi.edit: ['admin', 'supadmin'],
    Userapi.select: ['admin', 'supadmin', 'nromal'],
    Userapi.delete: ['admin', 'nromal']
}


def ispermission(path, role, version='v1'):
    """
    判断权限的方法
    :param path:  接口path
    :param role:  用户角色
    :return:  拥有权限则返回True，否则就False
    """
    path = path.split('/' + version)[1]
    permission = RolePermission_v1.get(path)
    if role in permission:
        return True
    else:
        return False

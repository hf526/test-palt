from app.models.model import Role


def create_role():
    """
    主要用来建立角色权限
    :return:
    """
    supamdin = Role(role='supadmin')
    Role.add_update(supamdin)
    admin = Role(role='admin')
    Role.add_update(admin)
    normal = Role(role='normal')
    Role.add_update(normal)


if __name__ == '__main__':
    create_role()

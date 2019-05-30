"""
导入flask实例，orm实例，迁移库，命令行管理库
实例化APP,配置数据库链接地址
实例化db对象
manager添加命令行实例
创建迁移脚本绑定app和db，添加命令
"""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.app import db
from app.apilist import app

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    app.run()

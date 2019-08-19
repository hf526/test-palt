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
from flask_socketio import SocketIO,send, emit

manager = Manager(app)
migrate = Migrate(app, db)

socketio = SocketIO(app)
manager.add_command('db', MigrateCommand)
manager.add_command('run', socketio.run(app=app, host='0.0.0.0', port=5000)) # 新加入的内容
import time

@socketio.on('connect', namespace='/test_conn')
def test_connect():
    while True:
        socketio.sleep(5)
        socketio.emit('server_response',
                      {'data': 1},
                      namespace='/test_conn')

@socketio.on('message')
def handle_message(msg):
    print('received message: ' + msg)

@socketio.on('json')
def handle_json(json):
    send(json, json=True)

if __name__ == "__main__":
    manager.run()

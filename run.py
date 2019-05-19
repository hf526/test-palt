from app.exts import app
import os


def inputc():
    system = input()
    if system == "init":
        os.system("python manage.py db init")
        os.system("python manage.py db migrate")
        os.system("python manage.py db upgrade")
    elif system == "update":
        os.system("python manage.py db migrate")
        os.system("python manage.py db upgrade")
    elif system == "back":
        os.system("python manage.py db downgrade")
    elif system == "api":
        os.system("apidoc -i views/ -o static/apidoc")
    elif system == "run":
        os.system("python manage.py runserver")
    else:
        inputc()


if __name__ == '__main__':
    inputc()
    # app.run()

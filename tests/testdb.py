from app.models.back.User_model import User

user = User.query.filter_by(username='test1').first()
print(user.name)
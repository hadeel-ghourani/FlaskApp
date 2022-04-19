from werkzeug.security import safe_str_cmp

from application.models.user import UserModel


def authenticate(username, password):
    user = UserModel.find(name=username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(Payload):
    user_id = Payload['identity']
    return UserModel.find(id=user_id)

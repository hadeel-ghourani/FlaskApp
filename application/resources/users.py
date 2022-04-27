from flask_restplus import Namespace, Resource, fields

from application.config import auth
from application.models.users import UserModel

user_ns = Namespace('register', description='registration',
                    authorizations=auth)

user = user_ns.model('UserRegister', {
    'id': fields.Integer(readonly=True,
                         description='The task unique identifier'),
    'username': fields.String(required=True, description='The store name.'),
    'password': fields.String(required=True, description='The store name.')
})


class UserRegister(Resource):

    @user_ns.doc('create_user')
    @user_ns.expect(user)
    def post(self):

        data = user_ns.payload
        name = data['username']
        password = data['password']

        if UserModel.find(name=name):
            return {"message": "User already exists!"}

        user = UserModel(name=name, password=password)

        user.insert()

        return user.json(), 200


user_ns.add_resource(UserRegister, '/')

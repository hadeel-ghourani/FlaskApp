import sys


from flask import Flask
from flask_jwt import JWT
from werkzeug.utils import cached_property
from flask_restplus import Api


from .config import auth, db_url
from .resources.items import item_ns
from .resources.stores import store_ns
from .resources.users import user_ns
from .security import authenticate, identity
from flask import jsonify

sys.path.append('.')
sys.setrecursionlimit(5000*10)


def create_app():
    app = Flask(__name__)
    api = Api(app, authorizations=auth, title="Simple Store API", base_url='/')
    app.secret_key = 'jose'
    app.config['SECRET_KEY'] = 'jose'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URL'] = db_url
    jwt = JWT(app, authenticate, identity)
    jwt.init_app(app)
    api.add_namespace(item_ns)
    api.add_namespace(store_ns)
    api.add_namespace(user_ns)

    return app


app = create_app()


@app.route("/", methods=['GET'])
def get_value():
    return jsonify("some_value"), 200
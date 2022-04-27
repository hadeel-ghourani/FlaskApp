import pytest
from application.main import create_app
from application.models.stores import StoreModel
from application.models.users import UserModel
from application.models.items import ItemModel


@pytest.fixture(scope='session')
def flask_app_mock():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(flask_app_mock):
    return flask_app_mock.test_client()


@pytest.fixture(scope='session')
def user_mock():
    user_model = UserModel(
        name="hadeel",
        password="123"
    )
    return user_model


@pytest.fixture(scope='session')
def store_mock():
    store_model = StoreModel(
        name='Store_A'
    )
    return store_model


@pytest.fixture(scope='session')
def item_mock():
    item_model = ItemModel(
        name='chair',
        price=123,
        serial_number='123456789a',
        store_id='941600af-1e8e-4e86-bba5-f29524b0496e'
    )
    return item_model


@pytest.fixture(scope='session')
def item_dict_mock():

    item_mock = {
        'name': 'chair',
        'price': 123,
        'serial_number': '123456789a',
        'store_id': '941600af-1e8e-4e86-bba5-f29524b0496e'
    }
    return item_mock


@pytest.fixture(scope='session')
def invalid_item_mock():
    invalid_item = {
        'name': 'chair',
        'price': -12,
        'serial_number': "235456abcd"
    }
    return invalid_item


@pytest.fixture(scope='session')
def store_dict_mock():

    item_mock = {
        'id': '941600af-1e8e-4e86-bba5-f29524b0496e',
        'name': 'Store_Q',
        'items': []
    }
    return item_mock

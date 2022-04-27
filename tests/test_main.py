from application.main import get_value


def test_flask_app_light_mock(flask_app_mock):

    with flask_app_mock.app_context():
        response = get_value()

    assert response[0].json == "some_value"

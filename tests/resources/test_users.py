from unittest.mock import patch


@patch("application.resources.users.UserRegister.post")
def test_post_user(post_user_mock, client, user_mock):

    post_user_mock.return_value = user_mock.json()
    response = client.post("/register/", data=user_mock.json())

    post_user_mock.assert_called()
    assert response.status_code == 200

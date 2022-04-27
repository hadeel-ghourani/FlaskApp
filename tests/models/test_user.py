from unittest import mock


class TestUserModel():

    def test_users_model(self, user_mock):
        """
        GIVEN a Users model
        WHEN a new User is created
        THEN check the name and password are defined correctly
        """
        assert user_mock.name == "hadeel"
        assert user_mock.password == "123"

    @mock.patch('application.models.users.UserModel.insert')
    def test_user_in_db(self, user_insertion_mock, user_mock):

        user_mock.insert()
        user_insertion_mock.assert_called()

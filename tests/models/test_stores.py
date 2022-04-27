from unittest.mock import patch


def test_users_model(store_mock):
    """
    GIVEN a Stores model
    WHEN a new Store is created
    THEN check the name is defined correctly
    """

    assert store_mock.name == "Store_A"


@patch("application.models.stores.StoreModel.insert")
def test_store_in_db(store_insertion_mock, store_mock):
    """
    GIVEN a Stores model
    WHEN a new Store is inserted
    THEN check the name is exist in database
    """

    store_mock.insert()
    store_insertion_mock.assert_called()

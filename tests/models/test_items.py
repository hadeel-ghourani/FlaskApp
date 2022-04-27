from unittest.mock import patch


def test_items_model(item_mock):
    """
    GIVEN a Items model
    WHEN a new Item is created
    THEN check the name and price are defined correctly
    """

    assert item_mock.name == 'chair'
    assert item_mock.price == 123
    assert item_mock.serial_number == '123456789a'
    assert item_mock.store_id == '941600af-1e8e-4e86-bba5-f29524b0496e'


@patch("application.models.items.ItemModel.insert")
def test_item_in_db(item_insertion_mock, item_mock):
    """
    GIVEN a Items model
    WHEN a new Item is inserted
    THEN check the name and price are exist in database
    """
    item_mock.insert()
    item_insertion_mock.assert_called()

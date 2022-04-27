from application.validation.item import ItemSchema


def test_valid_item(item_dict_mock):

    item = ItemSchema().load(item_dict_mock)

    assert item.get('name', None) == item_dict_mock.get('name', None)
    assert item.get('price', None) == item_dict_mock.get('price', None)
    assert item.get('serial_number', None) == item_dict_mock.get(
                                                        'serial_number', None)


# def test_invalid_item(invalid_item_mock):
    # ItemSchema().load(invalid_item_mock)

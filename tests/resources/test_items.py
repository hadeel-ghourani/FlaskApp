from unittest.mock import patch


@patch("application.resources.items.Item.get")
def test_get_item(get_item_mock, client, item_dict_mock):

    get_item_mock.return_value = item_dict_mock
    id = item_dict_mock.get('id', None)
    url = "/items/{}".format(id)
    response = client.get(url)

    get_item_mock.assert_called()
    assert response.status_code == 200


@patch("application.resources.items.Item.patch")
def test_patch_items(patch_item_mock, client, item_dict_mock):

    patch_item_mock.return_value = item_dict_mock
    id = item_dict_mock.get('id', None)
    url = "/items/{}".format(id)
    response = client.patch(url)

    patch_item_mock.assert_called()
    assert response.status_code == 200


@patch("application.resources.items.Item.delete")
def test_delete_items(delete_item_mock, client, item_dict_mock):

    delete_item_mock.return_value = item_dict_mock
    id = item_dict_mock.get('id', None)
    url = "/items/{}".format(id)
    response = client.delete(url)

    delete_item_mock.assert_called()
    assert response.status_code == 200


@patch("application.resources.items.ItemsList.get")
def test_get_items(get_itemsList_mock, client, item_dict_mock):

    get_itemsList_mock.return_value = item_dict_mock
    url = "/items/"
    response = client.get(url)

    get_itemsList_mock.assert_called()
    assert response.status_code == 200


@patch("application.resources.items.ItemsList.put")
def test_put_items(put_itemsList_mock, client, item_dict_mock):

    put_itemsList_mock.return_value = item_dict_mock
    url = "/items/"
    response = client.put(url)

    put_itemsList_mock.assert_called()
    assert response.status_code == 200


@patch("application.resources.items.ItemsList.put")
def test_post_items(post_itemsList_mock, client, item_dict_mock):

    post_itemsList_mock.return_value = item_dict_mock
    url = "/items/"
    response = client.post(url)

    post_itemsList_mock.assert_called()
    assert response.status_code == 201

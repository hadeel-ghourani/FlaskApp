from unittest.mock import patch


@patch("application.resources.stores.Store.get")
def test_get_store(get_store_mock, client, store_dict_mock):

    get_store_mock.return_value = store_dict_mock
    id = store_dict_mock.get('id', None)
    url = "/stores/{}".format(id)
    response = client.get(url)

    get_store_mock.assert_called()
    assert response.status_code == 200


@patch("application.resources.stores.Store.delete")
def test_delete_store(delete_store_mock, client, store_dict_mock):

    delete_store_mock.return_value = store_dict_mock
    id = store_dict_mock.get('id', None)
    response = client.delete("/stores/{}".format(id))

    delete_store_mock.assert_called()
    assert response.status_code == 200


@patch("application.resources.stores.StoreList.get")
def test_get_stores(get_stores_mock, client, store_dict_mock):

    get_stores_mock.return_value = store_dict_mock
    response = client.get("/stores/")

    get_stores_mock.assert_called()
    assert response.status_code == 200


@patch("application.resources.stores.StoreList.post")
def test_post_item(post_stores_mock, client, store_dict_mock):

    post_stores_mock.return_value = store_dict_mock
    response = client.post("/stores/",
                           data=store_dict_mock)

    post_stores_mock.assert_called()
    assert response.status_code == 200

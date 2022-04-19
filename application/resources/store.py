from flask_restplus import Namespace, Resource, fields

from application.config import auth
from application.models.store import StoreModel

from .item import item_field

store_ns = Namespace('store', description='registration', authorizations=auth)
stores_ns = Namespace('stores', description='registration',
                      authorizations=auth)
store = stores_ns.model('Store', {
    'name': fields.String(required=True, description='The store name.'),
    'items': fields.List(fields.Nested(item_field)),
})


class Store(Resource):

    @store_ns.doc('get_store')
    def get(self, id):

        store = StoreModel.find(id=id)
        if store:
            return store.json(), 200
        return {'message': 'Store not found'}, 404

    @store_ns.doc('Delete Store')
    def delete(self, id):

        store = StoreModel.find(id=id)
        if store:
            store.delete()
            return {'message': 'Store deleted'}, 200
        return {'message': 'The store you aim to delete not found!'}, 404


class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(),
                                   StoreModel.query.all()))}

    def post(self):

        data = store_ns.payload
        if StoreModel.find(name=data['name']):
            return {'message': "A store with name '{}' already exists."
                    .format(data['name'])}, 400

        store = StoreModel(**data)
        store.insert()
        return store.json(), 201


store_ns.add_resource(Store, '/<string:id>')
store_ns.add_resource(StoreList, '/')

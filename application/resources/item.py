import sys

from flask_jwt import jwt_required
from flask_restplus import Namespace, Resource, fields, reqparse

from application.config import auth
from application.models.base import session
from application.models.item import ItemModel
from application.validation.item import ItemSchema, NestedSchema

sys.path.append('.')


item_ns = Namespace('item', description='singel resource',
                    authorizations=auth)

item_field = item_ns.model('Item', {
    'id': fields.String(readonly=True,
                        description='The task unique identifier'),
    'name': fields.String(required=True, description='The store name.'),
    'price': fields.Float(required=True, description='The store name.'),
    'store_id': fields.String(required=True, description='The store name.'),
    'serial_number': fields.String(required=True,
                                   description="Item's serial number")
})
items_model = item_ns.model('Item', {
    'items': fields.List(fields.Nested(item_field)),
})


class Item(Resource):

    @item_ns.doc(security='Bearer Auth', body=item_field)
    @item_ns.doc('Get Item By ID')
    def get(self, id):

        item = ItemModel.find(id=id)
        if item:
            return item.json(), 200
        return {"msg": "Item {} not found".format(id)}, 404

    @item_ns.expect(item_field)
    def patch(self, id):

        data = item_ns.payload
        item = ItemModel.find(id=id)
        if item:
            ItemSchema().load(data)
            item.update(**data)
            return item.json()
            # except:
            #    return {"message": "An error occurred creating the item."},
            # 500
        return {'msg': 'Item is not found!'}

    # @jwt_required()
    @item_ns.doc(security='Bearer Auth')
    @item_ns.doc('Delete Item By ID')
    def delete(self, id):

        item = ItemModel.find(id=id)
        if item:
            item.delete()
            return {'message': 'Item has been deleted '}, 200
        return {'message': 'Item does not exist'}, 404


class ItemsList(Resource):

    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

    # @jwt_required()
    @item_ns.doc(security='Bearer Auth')
    @item_ns.doc('Update Item')
    @item_ns.expect(items_model)
    def put(self):

        requested_data = item_ns.payload
        success = []
        fail = []

        loaded_items = NestedSchema().load(requested_data)

        for unvalidated_item in loaded_items['items']:
            try:
                _item = ItemSchema().load(unvalidated_item)
            except Exception as e:
                fail.append(dict(unvalidated_item, error=str(e)))
                continue
            query = ItemModel.find(serial_number=_item['serial_number'],
                                   name=_item['name'])
            if query:
                query.update(**_item)
                success.append(dict(Item_ID=query.id, status=200))
            else:
                new_item = ItemModel(**_item)
                new_item.insert()
                success.append(dict(Item_ID=new_item.name, status=201))
        return {"Updated Items": success, "Failed to update": fail}

    # @jwt_required()
    # @item_ns.doc(security='Bearer Auth')
    @item_ns.doc('Greate Item')
    @item_ns.expect(item_field)
    def post(self):

        data = item_ns.payload
        item = ItemModel.find(id=data.get(id, None))
        try:

            loaded_data = ItemSchema().load(data)
            item = ItemModel.find(name=loaded_data['name'])
            if item:
                return {'message': "Item already exists."}, 400
            item = ItemModel(**data)
            item.insert()
            return item.json()
        except Exception:
            return {"msg": "err.args"}


item_ns.add_resource(Item, '/<string:id>')
item_ns.add_resource(ItemsList, '/')

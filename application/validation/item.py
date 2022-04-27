import sys

from marshmallow import Schema, ValidationError, fields, validate, validates

from application.models.items import ItemModel

from .base import BaseSchema

sys.path.append('.')


class ItemSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = ItemModel
        include_fk = True

    name = fields.String(validate=validate.Length(max=50))
    price = fields.Float()
    store_id = fields.String()
    serial_number = fields.String()

    @validates('name')
    def validate_name(self, data):
        if len(data) > 50:
            raise ValidationError("The name is not valid, too long!")

    @validates('price')
    def validate_price(self, data):
        if data <= 0:
            raise ValidationError(
                'The price is not valid, must be great than ZERO!')

    @validates('serial_number')
    def validate_serial(self, data):
        if len(data) != 10:
            raise ValidationError(
                'Serial Number is not valid length, must be 10 characters!')
        try:
            int(data, 16)
        except ValueError:
            raise ValidationError
        ('Serial Number is not valid, must be in hex!')


class NestedSchema(Schema):
    items = fields.List(fields.Dict)

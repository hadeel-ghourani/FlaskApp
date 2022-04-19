import sys

from marshmallow_sqlalchemy import SQLAlchemySchema

from application.models.base import BaseModel

sys.path.append('.')


class BaseSchema(SQLAlchemySchema):
    class Meta:
        model = BaseModel
        abstract = True

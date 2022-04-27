import sys

from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import BaseModel
from .stores import StoreModel

sys.path.append('.')


class ItemModel(BaseModel):

    __tablename__ = "items"

    def __init__(self, **data):
        super().__init__(data['name'])
        self.price = data['price']
        self.serial_number = data['serial_number']
        self.store_id = data['store_id']

    price = Column(Float)
    store_id = Column(UUID(as_uuid=True), ForeignKey('stores.id'))
    serial_number = Column(String)
    stores = relationship(StoreModel, back_populates='items')

    def json(self):
        return {"Item ID ": str(self.id), "Item Name  ": self.name,
                "Item price": self.price,
                "Serial Number": self.serial_number,
                "Store ID  ": str(self.store_id),
                "Created at  ": str(self.created_at),
                "Updated at  ": str(self.updated_at)}

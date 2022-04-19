import sys

from sqlalchemy.orm import relationship

from .base import BaseModel

sys.path.append('.')


class StoreModel(BaseModel):
    __tablename__ = "stores"

    items = relationship('ItemModel', cascade='all, delete', lazy='dynamic')

    def __init__(self, name):
        super().__init__(name)

    def json(self):
        return {"Name": self.name, "ID": str(self.id),
                "Created at": str(self.created_at),
                "Updated at": str(self.updated_at),
                "Items: ": [item.json() for item in self.items.all()]}

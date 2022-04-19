import sys

from sqlalchemy import Column, String

from .base import Base, BaseModel, engine

sys.path.append('.')


class UserModel(BaseModel):

    __tablename__ = "users"

    def __init__(self, name, password):
        super().__init__(name)
        self.password = password

    password = Column(String)

    def json(self):
        return {"Name": self.name, "ID ": str(self.id),
                "created at": str(self.created_at),
                "Updated at": str(self.updated_at)}
#Base.metadata.create_all(bind=engine)

from .base import Base, engine, session
from .item import ItemModel
from .store import StoreModel
from .user import UserModel


def create_db():
    Base.metadata.create_all(bind=engine)
    
def drop_db():
    session.close_all()
    Base.metadata.drop_all(bind=engine)
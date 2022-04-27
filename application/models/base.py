import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql import func

from application.config import db_url

engine = create_engine(db_url)
session = scoped_session(sessionmaker(bind=engine, autocommit=False,
                                      autoflush=False))

Base = declarative_base()
Base.query = session.query_property()


class BaseModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    created_at = Column(DateTime(), default=datetime.datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, name):
        self.name = name

    @classmethod
    def find(cls, **criterions):
        return cls.query.filter_by(**criterions).first()

    def insert(self):
        session.add(self)
        session.commit()
        #return self.name

    def update(self, **data):
        self.query.update(data)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    def get_id(self):
        return self.id

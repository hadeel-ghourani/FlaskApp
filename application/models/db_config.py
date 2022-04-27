from os import environ
import sys
from sqlalchemy.engine import create_engine


sys.path.append('.')

POSTGRES_HOST = environ.get('POSTGRES_HOST')
POSTGRES_USER = environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
POSTGRES_PORT = environ.get('POSTGRES_PORT')
POSTGRES_DB = environ.get('POSTGRES_DB')

db_url = 'postgresql+psycopg2://{}:{}@{}:5432/{}'.format(POSTGRES_USER,
                                                         POSTGRES_PASSWORD,
                                                         POSTGRES_HOST,
                                                         POSTGRES_DB)

# engine = create_engine(db_url)

import sys
from os import environ

sys.path.append('.')

auth = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'bearerFormat': 'JWT',
        'description':
            "Type in the 'Value' input box below: **'JWT &lt;JWT&gt;'**,"
            "where JWT is the token"
    },
}

POSTGRES_HOST = environ.get('POSTGRES_HOST')
POSTGRES_USER = environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
POSTGRES_PORT = environ.get('POSTGRES_PORT')
POSTGRES_DB = environ.get('POSTGRES_DB')


db_url = 'postgresql+psycopg2://{}:{}@{}:5432/{}'.format(POSTGRES_USER,
                                                         POSTGRES_PASSWORD,
                                                         POSTGRES_HOST,
                                                         POSTGRES_DB)


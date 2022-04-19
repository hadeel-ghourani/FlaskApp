#!/bin/sh
chmod 701 bin/wait-for-it.sh 
./bin/wait-for-it.sh $POSTGRES_HOST:$POSTGRES_PORT -- echo "Postgres is up"
#alembic revision --autogenerate -m "db"
#alembic upgrade head
python3 -m gunicorn --preload -w 5 --threads 5 --bind 0.0.0.0:80 --timeout 90 --chdir .. application.wsgi:app

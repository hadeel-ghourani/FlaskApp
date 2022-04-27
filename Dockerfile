FROM python:3.6.8

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

RUN pip install psycopg2

ADD . .

EXPOSE 80

ENTRYPOINT [ "./bin/test.sh" ]


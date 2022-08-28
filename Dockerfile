FROM python:3.10.6-slim-buster

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
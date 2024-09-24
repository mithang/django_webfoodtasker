FROM python:3.8-slim

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt



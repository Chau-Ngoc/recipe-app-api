FROM python:3.9-slim
MAINTAINER Chau Le

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apt-get install postgresql-client python3-dev libpq-dev

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /djangobackend

COPY /djangobackend/ /djangobackend

WORKDIR /djangobackend

RUN pip3 install -r requirements.txt
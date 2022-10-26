FROM python:3.10.1-slim-buster

COPY ./src/requirements.txt /api/requirements.txt

WORKDIR /api

ARG WORKERS_ARG
ENV WORKERS=$WORKERS_ARG

ENV PORT=8080


RUN apt-get update \
&& apt-get install -y --no-install-recommends git \
&& apt-get purge -y --auto-remove \
&& rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt --no-cache-dir
RUN pip install gunicorn

COPY ./src /api/src

ENV PYTHONPATH=$(pwd)
ENV PYTHONUNBUFFERED=1

EXPOSE 8080

RUN mkdir -p /api/src/logs
RUN chmod 777 -R /api/src/

VOLUME /api/src

ENTRYPOINT gunicorn --workers $WORKERS --bind 0.0.0.0:8080 --chdir ./src wsgi:app

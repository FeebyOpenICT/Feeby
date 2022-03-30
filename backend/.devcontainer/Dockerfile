FROM python:3.9-slim as base

# Install deps for psycopg2 and git
RUN apt-get update \
    && apt-get -y install libpq-dev gcc git

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

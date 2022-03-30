FROM python:3.9-slim as base

# Install deps for psycopg2
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./app /app


FROM base as development 
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
WORKDIR /app
CMD uvicorn main:app --proxy-headers --reload --host 0.0.0.0 --port 80


FROM base as debug
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
RUN pip install debugpy
WORKDIR /app
CMD python -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m uvicorn main:app --reload --host 0.0.0.0 --port 80


FROM base as production
WORKDIR /app
RUN PYTHONPATH=. pytest
EXPOSE 80
CMD uvicorn main:app --proxy-headers --host 0.0.0.0 --port 80

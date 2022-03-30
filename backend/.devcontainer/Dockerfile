#The base image for the container
FROM python:3.9-slim-buster as development
ENV PYTHONPATH=app
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1
# Install deps for psycopg2
RUN apt-get update 
RUN apt-get install -y gcc g++ libpq-dev gcc git python3-dev
# Copy python requirements to the docker container and install
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
#create a non root user to access the container
RUN adduser --uid 5678 --disabled-password --gecos "" vscode
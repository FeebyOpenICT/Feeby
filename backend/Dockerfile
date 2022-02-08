FROM python:3.9 as development

WORKDIR /development

COPY ./requirements.txt /development/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /development/requirements.txt

COPY ./app /development/app

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--reload", "--host", "0.0.0.0", "--port", "80"]

FROM python:3.9-slim as testing

WORKDIR /testing

COPY ./requirements.txt /testing/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /testing/requirements.txt

COPY ./app /testing/app

RUN ["pytest"]

FROM python:3.9-alpine as production

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY --from=testing /testing/app /code/app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

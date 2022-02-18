FROM python:3.9-alpine as base

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

FROM base as development

RUN pip install ptvsd

WORKDIR /app
CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m uvicorn main:app --proxy-headers --host 0.0.0.0 --port 80

FROM base as production

WORKDIR /app

RUN ["pytest"]

EXPOSE 80

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

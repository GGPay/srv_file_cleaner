FROM tiangolo/uvicorn-gunicorn:python3.9-alpine3.14

RUN apk update && apk add openssl-dev cargo musl-dev python3-dev gcc libffi-dev g++ postgresql-dev make curl

RUN apk del libffi-dev g++ make curl

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./app /app/app

COPY ./app/settings/prestart.sh /app/prestart.sh
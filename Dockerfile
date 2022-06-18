FROM tiangolo/uvicorn-gunicorn:python3.9-alpine3.14

RUN apk update && apk add openssl-dev cargo musl-dev python3-dev gcc libffi-dev g++ postgresql-dev make curl

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN source $HOME/.poetry/env && poetry config virtualenvs.create false && poetry install --no-dev --no-ansi --no-root

RUN apk del libffi-dev g++ make curl

COPY ./app /app/app

COPY ./alembic.ini /app/alembic.ini

COPY ./app/settings/prestart.sh /app/prestart.sh
from fastapi import FastAPI
from gino.ext.starlette import Gino
from sqlalchemy.schema import MetaData
from starlette.datastructures import Secret

from .settings.globals import DATABASE_CONFIG

app: FastAPI = FastAPI(title='Data Crunch Application',
                       description='Service for cleaning and matching description with database',
                       version='0.0.1')

db: MetaData = Gino(app, dsn=DATABASE_CONFIG.url)

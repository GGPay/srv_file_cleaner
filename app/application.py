from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.settings.globals import DATABASE_CONFIG


app: FastAPI = FastAPI(title='Application',
                       description='Service for check description in database',
                       version='0.0.1')

engine = create_async_engine(
    DATABASE_CONFIG.url
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


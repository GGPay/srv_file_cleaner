from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.dependencies.db import get_db



router = APIRouter()


@router.get("/product", status_code=status.HTTP_200_OK, tags=["Products"])
async def get_product_matching_score(word: str, db: AsyncSession = Depends(get_db)):
    #code: ORMSpKod = await ORMSpKod.get(id)
    return


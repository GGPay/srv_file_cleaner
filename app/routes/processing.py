from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.dependencies.db import get_db
from app.models.orm.db_schema import Product as ORMProduct
from app.models.pydantic.product import ProductModel
from sqlalchemy import select


router = APIRouter()


@router.get("/product", status_code=status.HTTP_200_OK, tags=["Products"])
async def get_product_matching_score(word: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ORMProduct).where(ORMProduct.partNumber == word))
    product_id = result.scalars().first()
    return ProductModel.from_orm(product_id)

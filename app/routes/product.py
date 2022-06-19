from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.dependencies.db import get_db
from app.models.orm.queries import product as product_utils


router = APIRouter()


@router.get("/product", status_code=status.HTTP_200_OK, tags=["Products"])
async def get_product_matching_score(part_number: str, factory_id: int, db: AsyncSession = Depends(get_db)):
    products = await product_utils.get_products_by_factory_id(factory_id, db)

    return products

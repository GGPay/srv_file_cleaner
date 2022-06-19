from sqlalchemy import select
from app.models.orm.db_schema import Product as ORMProduct
from app.models.pydantic.product import ProductModel


async def get_products_by_factory_id(id, db):

    result = await db.execute(select(ORMProduct).where(ORMProduct.factoryID == id))
    products = result.scalars().all()

    context = []
    i = 0
    for _ in products:
        context.append(ProductModel.from_orm(products[i]).dict())
        i += 1

    return context

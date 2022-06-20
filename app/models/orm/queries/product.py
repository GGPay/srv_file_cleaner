from app.models.pydantic.product import ProductModel


async def get_products_by_factory_id(id, db):

    stmt = 'select DISTINCT ordd."description", pr."partNumber", pr."factoryID"' \
           'from "order" ord, "orderDetails" ordd, "product" pr ' \
           'where ord."orderID" = ordd."orderID" ' \
           'and pr."productID" = ordd."productID" ' \
           'and pr."factoryID" = ' + str(id)

    result = await db.execute(stmt)
    products = result.all()

    context = []
    i = 0
    for _ in products:
        context.append(ProductModel.from_orm(products[i]).dict())
        i += 1

    return context

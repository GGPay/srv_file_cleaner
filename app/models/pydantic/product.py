from pydantic import BaseModel, Field


class ProductModel(BaseModel):
    productID: int = Field(..., alias='product_id')
    factoryID: int = Field(..., alias='factory_id')
    partNumber: str = Field(..., alias='part_number')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

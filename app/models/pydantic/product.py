from pydantic import BaseModel, Field, NoneStr


class ProductModel(BaseModel):
    description: NoneStr = Field(..., alias='description')
    factoryID: int = Field(..., alias='factory_id')
    partNumber: str = Field(..., alias='part_number')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

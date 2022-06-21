from pydantic import BaseModel, Field, NoneStr
from typing import Dict


class ProductModel(BaseModel):
    description: NoneStr = Field(..., alias='description')
    factoryID: int = Field(..., alias='factory_id')
    partNumber: str = Field(..., alias='part_number')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RepositoryDetail(BaseModel):
    factoryID: int
    target_partNumber: str = Field(..., alias='target_part_number')
    partNumber: str = Field(..., alias='part_number')
    match_score: float
    description: str = Field(..., alias='description')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

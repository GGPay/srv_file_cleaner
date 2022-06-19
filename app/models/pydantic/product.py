from datetime import datetime
from pydantic import BaseModel, Field
from typing import Dict


class ProductModel(BaseModel):
    productID: int = Field(..., alias='product_id')
    partNumber: str = Field(..., alias='part_number')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class CodeFullDetailModel(BaseModel):
    id: int
    date_b: datetime
    date_e: datetime = None
    id_sp_kod: int = Field(..., alias='code_id')
    name: str = Field(..., alias='description')
    flag: int

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RepositoryDetail(BaseModel):
    id: int
    id_channel_updates: int
    id_sp_kod: int = Field(..., alias='code_id')
    value_json: Dict = Field(..., alias='values')
    blockchain: Dict = None
    name: str = None
    created: datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True



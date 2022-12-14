from fastapi import APIRouter, Depends, HTTPException
from typing import List
import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from app.dependencies.db import get_db
from app.models.orm.queries import product as product_utils
from app.backend.utils import StringClean
from app.models.pydantic.product import RepositoryDetail
import app.backend.feature_extractor as fe

router = APIRouter()


@router.get("/product", status_code=status.HTTP_200_OK, tags=["Products"], response_model=List[RepositoryDetail])
async def get_product_matching_score(part_number: str, factory_id: int, db: AsyncSession = Depends(get_db)):

    products = await product_utils.get_products_by_factory_id(factory_id, db)
    clean_part_num = StringClean.clean_string(part_number)

    if len(products) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No found any part numbers for factoryID")

    df_result = pd.DataFrame()
    df = pd.DataFrame.from_dict(products)
    df.loc[:, 'target_partNumber'] = clean_part_num
    # we shall apply some cleaning logic to db dataset
    df['partNumber'] = df['partNumber'].str.lstrip('0').fillna(value='0')

    # calculate levenstein distance and score
    df['levenshtein_distance'] = df.apply(fe.sorted_levenshtein_apply, axis=1)
    df['unique_number_count'] = df.apply(fe.get_unique_number_count, axis=1) + 1
    df['number_match_rate'] = df.apply(fe.get_rate, axis=1)
    df['match_score'] = df.apply(fe.sorted_levenshtein_rate_apply, axis=1)
    cols = ['factoryID', 'partNumber', 'target_partNumber', 'match_score', 'description']
    df = df.nlargest(3, 'match_score')
    df_result = df[cols]

    product_score = df_result.to_dict('records')

    context = []
    i = 0
    for _ in product_score:
        context.append(RepositoryDetail.parse_obj(product_score[i]).dict())
        i += 1

    return context


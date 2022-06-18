from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..models.orm.user import User as ORMUser
from ..models.orm.user import Token as ORMToken
from ..models.orm.queries import user as users_utils
from ..models.pydantic.user import User, UserCreateIn, Token
from ..settings.globals import ACCESS_TOKEN_EXPIRE_MINUTES

from .. security.dependencies import get_current_active_user


router = APIRouter()


@router.post("/login", tags=["Authentication"], response_model=Token, response_model_include=["token"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_utils.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or hashed_password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await users_utils.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    payload = {"token": access_token['token'], "expires": access_token['expires'], "user_id": user.id}
    token: ORMToken = await ORMToken.create(**payload)
    return {"access_token": access_token['token'], "token_type": "bearer"}


@router.post("/sign_up", tags=["Users"], response_model=User, include_in_schema=True)
async def create_user(request: UserCreateIn):
    db_user = await users_utils.get_user_by_email(email=request.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email already registered")
    request.hashed_password = users_utils.get_password_hash(request.hashed_password)
    new_user: ORMUser = await ORMUser.create(**request.dict())
    return User.from_orm(new_user)


@router.get("/users/me", tags=["Users"], response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

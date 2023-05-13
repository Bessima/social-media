import time
from typing import TYPE_CHECKING

import jwt
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from social_media.core import get_session
from social_media.core.settings import config
from social_media.repositories import UserRepository
from social_media.tables.schemas import UserCreateSchema, UserLoginSchema
from social_media.validators import UserValidator

if TYPE_CHECKING:
    from social_media.tables import User

router = APIRouter()


def token_response(token: str):
    return {"access_token": token}


def sign_jwt(user_id: str) -> dict[str, str]:
    payload = {"user_id": user_id, "expires": time.time() + 600}
    token = jwt.encode(payload, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)

    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


@router.post("/user/register")
async def create_user(
    user_schema: UserCreateSchema, session: 'AsyncSession' = Depends(get_session)
):
    repository = UserRepository(session)
    user: 'User' = await repository.create(user_schema)

    return JSONResponse(content={"user_id": user.id})


@router.post("/login")
async def login(user_schema: UserLoginSchema, session: 'AsyncSession' = Depends(get_session)):
    validator = UserValidator(repository=UserRepository(session))
    await validator.validate(user_schema)

    return JSONResponse(content=sign_jwt(str(user_schema.user_id)))


@router.get("/user/get/{id}")
async def get_user(id):
    pass

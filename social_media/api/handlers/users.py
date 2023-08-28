from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from social_media.core import get_read_session, get_session
from social_media.core.auth import JWTBearer, sign_jwt
from social_media.repositories import UserRepository
from social_media.tables.schemas import UserCreateSchema, UserLoginSchema, UserResponse, Users
from social_media.validators import UserValidator

if TYPE_CHECKING:
    from social_media.tables import User

router = APIRouter()


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
async def get_user(id: str, session: 'AsyncSession' = Depends(get_session)):
    validator = UserValidator(repository=UserRepository(session))
    user = await validator.validate_user_id(id)

    return UserResponse.from_orm(user)


@router.get("/user/search")
async def get_user(
    first_name: str, last_name: str, session: 'AsyncSession' = Depends(get_session)
):
    users = await UserRepository(session).get_like_by_name_and_surname(
        first_name=first_name,
        second_name=last_name,
    )

    return Users(users=users)

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from social_media.core import get_session
from social_media.core.auth import JWTBearer, get_user_id
from social_media.repositories import FriendRepository, UserRepository
from social_media.validators import FriendValidator, UserValidator

router = APIRouter()


@router.post("/friend/set/{friend_id}")
async def add_friend(
    friend_id: UUID,
    token: Annotated[str, Depends(JWTBearer())],
    session: 'AsyncSession' = Depends(get_session),
):
    user_id = get_user_id(token)
    repository = FriendRepository(session)
    await repository.add(user_id=user_id, friend_id=str(friend_id))

    return JSONResponse(content={"msg": "Пользователь успешно указал своего друга"})


@router.delete("/friend/delete/{friend_id}")
async def delete_friend(
    friend_id: UUID,
    token: Annotated[str, Depends(JWTBearer())],
    session: 'AsyncSession' = Depends(get_session),
):
    user_id = get_user_id(token)
    validator = UserValidator(repository=UserRepository(session))
    await validator.validate_user_id(user_id)

    repository = FriendRepository(session)
    friend_validator = FriendValidator(repository=repository, user_id=user_id)
    await friend_validator.validate_friend(friend_id=str(friend_id))

    await repository.delete(user_id=user_id, friend_id=friend_id)

    return JSONResponse(content={"msg": "Пользователь успешно удалил из друзей пользователя"})

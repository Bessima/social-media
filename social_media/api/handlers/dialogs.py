from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from social_media.core import get_session
from social_media.core.auth import JWTBearer, get_user_id
from social_media.repositories import DialogRepository, UserRepository
from social_media.tables.schemas import DialogResponseSchema, DialogSchema
from social_media.validators import UserValidator

router = APIRouter()


@router.post("/dialog/{opponent_id}/send")
async def send_message(
    opponent_id: UUID,
    dialog_schema: DialogSchema,
    token: Annotated[str, Depends(JWTBearer())],
    session: 'AsyncSession' = Depends(get_session),
):
    opponent_id = str(opponent_id)
    user_id = get_user_id(token)
    validator = UserValidator(repository=UserRepository(session))
    await validator.validate_user_id(user_id)
    await validator.validate_user_id(opponent_id)

    await DialogRepository(session).add(user_id, opponent_id, dialog_schema.message)

    return JSONResponse(content={"msg": "Успешно отправлено сообщение"})


@router.get("/dialog/{opponent_id}/list")
async def get_dialog(
    opponent_id: UUID,
    token: Annotated[str, Depends(JWTBearer())],
    session: 'AsyncSession' = Depends(get_session),
):
    opponent_id = str(opponent_id)
    user_id = get_user_id(token)
    validator = UserValidator(repository=UserRepository(session))
    await validator.validate_user_id(user_id)
    await validator.validate_user_id(str(opponent_id))

    messages = await DialogRepository(session).get_messages(
        user_id=user_id,
        opponent_id=opponent_id,
    )
    return DialogResponseSchema(messages=messages)

from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from social_media.core import get_session
from social_media.core.auth import JWTBearer, get_user_id
from social_media.repositories import PostRepository, UserRepository
from social_media.tables.schemas.post import PostFullSchema, PostSchema
from social_media.validators import PostValidator, UserValidator

router = APIRouter()


@router.post("/post/create")
async def create(
    post_schema: PostSchema,
    token: Annotated[str, Depends(JWTBearer())],
    session: 'AsyncSession' = Depends(get_session),
):
    schema = PostFullSchema(author_id=get_user_id(token), text=post_schema.text)
    repository = PostRepository(session)
    await repository.create(schema)

    return JSONResponse(content="Успешно создан пост")


@router.put("/post/update/{post_id}")
async def update(
    post_id: UUID,
    post_schema: PostSchema,
    token: Annotated[str, Depends(JWTBearer())],
    session: 'AsyncSession' = Depends(get_session),
):
    author_id = get_user_id(token)

    repository = PostRepository(session)
    validator = PostValidator(repository)
    await validator.validate(post_id=str(post_id), author_id=author_id)
    await repository.update(id_=str(post_id), schema=post_schema)

    return JSONResponse(content="Успешно изменен пост")


@router.get("/post/get/{post_id}")
async def get(
    post_id: UUID,
    token: Annotated[str, Depends(JWTBearer())],
    session: 'AsyncSession' = Depends(get_session),
):
    author_id = get_user_id(token)

    repository = PostRepository(session)
    validator = PostValidator(repository)
    post = await validator.validate(post_id=str(post_id), author_id=author_id)

    return PostSchema.from_orm(post)


@router.delete("/post/delete/{post_id}")
async def delete(
    post_id: UUID,
    token: Annotated[str, Depends(JWTBearer())],
    session: 'AsyncSession' = Depends(get_session),
):
    author_id = get_user_id(token)
    repository = PostRepository(session)
    validator = PostValidator(repository)
    await validator.validate(post_id=str(post_id), author_id=author_id)

    await repository.delete(id=post_id)

    return JSONResponse(content={"msg": "Успешно удален пост"})


@router.get("/post/feed")
async def feed(
    token: Annotated[str, Depends(JWTBearer())],
    session: 'AsyncSession' = Depends(get_session),
):
    user_id = get_user_id(token)

    validator = UserValidator(repository=UserRepository(session))
    await validator.validate_user_id(user_id)

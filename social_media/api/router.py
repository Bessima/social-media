from fastapi import APIRouter

from social_media.api.handlers import dialogs_router, friend_router, post_router, user_router

api_router = APIRouter()

api_router.include_router(user_router, tags=["users"])
api_router.include_router(friend_router, tags=["friends"])
api_router.include_router(post_router, tags=["posts"])
api_router.include_router(dialogs_router, tags=["dialog"])

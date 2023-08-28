from fastapi import APIRouter

from social_media.api.handlers import friend_router, user_router

api_router = APIRouter()

api_router.include_router(user_router, tags=["users"])
api_router.include_router(friend_router, tags=["friends"])

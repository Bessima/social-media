from fastapi import APIRouter

from api.handlers import user_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/", tags=["users"])

from .friends import router as friend_router
from .users import router as user_router

__all__ = [
    'user_router',
    'friend_router',
]

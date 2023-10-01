from .dialogs import router as dialogs_router
from .friends import router as friend_router
from .posts import router as post_router
from .users import router as user_router

__all__ = [
    'user_router',
    'friend_router',
    'post_router',
    'dialogs_router',
]

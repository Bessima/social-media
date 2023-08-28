from social_media.tables import Friend

from .base import BaseRepository


class FriendRepository(BaseRepository):
    model = Friend

    async def add(self, user_id: str, friend_id: str):
        elem = self.model(user_id=user_id, friend_id=friend_id)
        try:
            self.session.add(elem)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        return elem

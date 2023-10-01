from sqlalchemy import and_, or_, select

from social_media.tables import Dialog

from .base import BaseRepository


class DialogRepository(BaseRepository):
    model = Dialog

    async def add(self, user_id: str, opponent_id: str, message: str):
        elem = self.model(user_id=user_id, opponent_id=opponent_id, message=message)
        try:
            self.session.add(elem)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
        return elem

    async def get_messages(self, user_id: str, opponent_id: str, limit: int = 10):
        query = (
            select(self.model)
            .where(
                or_(
                    and_(Dialog.user_id == user_id, Dialog.opponent_id == opponent_id),
                    and_(Dialog.user_id == opponent_id, Dialog.opponent_id == user_id),
                ),
            )
            .order_by(self.model.created_at)
            .limit(limit)
        )
        elems = await self.session.execute(query)
        return elems.scalars().all()

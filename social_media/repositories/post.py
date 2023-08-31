from pydantic import BaseModel
from sqlalchemy import update

from social_media.tables import Post

from .base import BaseRepository


class PostRepository(BaseRepository):
    model = Post

    async def update(self, id_: str, schema: BaseModel):
        try:
            query = update(self.model).where(self.model.id == id_).values(**schema.dict())
            await self.session.execute(query)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

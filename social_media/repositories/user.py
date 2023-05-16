from social_media.tables import User

from ..tables.schemas import UserCreateSchema
from .base import BaseRepository


class UserRepository(BaseRepository):
    model = User

    def update(self, id_: int, represent: User) -> User:
        pass

    async def create(self, represent: UserCreateSchema) -> User:
        user = self.model(**represent.dict())
        user.set_password(user.password)

        try:
            self.session.add(user)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

        return user

from sqlalchemy.future import select

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

    async def get_like_by_name_and_surname(self, first_name, second_name) -> []:
        query = select(self.model).filter(
            User.first_name.like(first_name + "%"),
            User.second_name.like(second_name + "%"),
        )
        elems = await self.session.execute(query)
        return elems.scalars().all()

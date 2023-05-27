from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from social_media.core.database import Base


class BaseRepository(ABC):
    """Main operation with tables."""

    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    async def update(self, id_: UUID, represent: BaseModel) -> Base:
        pass

    async def create(self, represent: BaseModel) -> Base:
        elem = self.model(**represent.dict())
        try:
            self.session.add(elem)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

        return elem

    async def get(self, id_: str) -> BaseModel or None:
        query = select(self.model).filter(self.model.id == id_)
        elems = await self.session.execute(query)
        return elems.scalar()

    async def get_by_fields(self, **kwargs) -> []:
        query = select(self.model).filter_by(**kwargs)
        elems = await self.session.execute(query)
        return elems.scalars().all()

    async def get_list(self) -> List[Base]:
        query = await self.session.execute(select(self.model))
        return query.scalars().all()

    async def delete(self, id_: UUID):
        query = select(self.model).filter(self.model.id == id_).delete()
        await self.session.execute(query)
        await self.session.commit()
        return True

    async def _record_object(self, model: Base):
        """Запись объекта в модель."""
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return model

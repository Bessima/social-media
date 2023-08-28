from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from social_media.core import Base


class Friend(Base):
    __tablename__ = "friends"

    user_id = Column(UUID, ForeignKey("users.id"), primary_key=True, nullable=False)
    friend_id = Column(UUID, ForeignKey("users.id"), primary_key=True, nullable=False)

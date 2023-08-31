from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from social_media.core import Base
from social_media.tables.utils import create_uuid


class Post(Base):
    __tablename__ = "posts"

    id = Column(UUID(), primary_key=True, index=True, default=create_uuid)
    text = Column(String, nullable=False)
    author_id = Column(UUID, ForeignKey("users.id"), primary_key=True, nullable=False)

    author = relationship("User", back_populates="posts")

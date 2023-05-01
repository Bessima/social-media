import uuid

from sqlalchemy import Column, DateTime, String, Integer, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from social_media.core import Base
from .enums import Gender


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    hobby = Column(Text, nullable=False)
    city = Column(String, nullable=False)

    time_created = Column(DateTime(timezone=True), server_default=func.now())

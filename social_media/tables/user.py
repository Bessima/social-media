import uuid

import bcrypt as bcrypt
from sqlalchemy import Column, DateTime, Enum, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from social_media.core import Base

from ..core.settings import config
from .enums import Gender


def create_uuid() -> str:
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(), primary_key=True, index=True, default=create_uuid)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    hobby = Column(Text, nullable=False)
    city = Column(String, nullable=False)
    password = Column(String, nullable=False)

    time_created = Column(DateTime(timezone=True), server_default=func.now())

    def set_password(self, value):
        self.password = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt()).decode()

    def check_password(self, inner_password):
        return bcrypt.checkpw(inner_password.encode('utf-8'), self.password.encode('utf-8'))

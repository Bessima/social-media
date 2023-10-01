from sqlalchemy import Column, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID

from social_media.core import Base


class Dialog(Base):
    __tablename__ = "dialogs"

    user_id = Column(UUID, ForeignKey("users.id"), primary_key=True, nullable=False)
    opponent_id = Column(UUID, ForeignKey("users.id"), primary_key=True, nullable=False)
    message = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), primary_key=True)

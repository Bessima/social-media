from datetime import datetime

from pydantic import BaseModel


class DialogSchema(BaseModel):
    message: str

    class Config:
        orm_mode = True


class MessageSchema(BaseModel):
    user_id: str
    opponent_id: str
    message: str
    created_at: datetime

    class Config:
        orm_mode = True


class DialogResponseSchema(BaseModel):
    messages: list[MessageSchema]

    class Config:
        orm_mode = True

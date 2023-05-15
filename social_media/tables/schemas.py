from uuid import UUID

from pydantic import BaseModel

from social_media.tables.enums import Gender


class UserCreateSchema(BaseModel):
    first_name: str
    second_name: str
    age: int
    gender: Gender
    hobby: str
    city: str
    password: str


class UserLoginSchema(BaseModel):
    user_id: UUID
    password: str


class UserResponse(BaseModel):
    first_name: str
    second_name: str
    age: int
    gender: Gender
    hobby: str
    city: str

    class Config:
        orm_mode = True

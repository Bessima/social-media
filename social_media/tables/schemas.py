from pydantic import BaseModel

from social_media.tables.enums import Gender


class UserSchema(BaseModel):
    first_name: str
    second_name: str
    age: int
    gender: Gender
    hobby: str
    city: str
    password: str


class UserLoginSchema(BaseModel):
    user_id: str
    password: str

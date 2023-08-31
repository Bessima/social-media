from pydantic import BaseModel


class PostSchema(BaseModel):
    text: str

    class Config:
        orm_mode = True


class PostFullSchema(PostSchema):
    author_id: str

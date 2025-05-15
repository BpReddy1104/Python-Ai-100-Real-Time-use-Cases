from pydantic import BaseModel, ConfigDict

class BlogBase(BaseModel):
    title: str
    content: str

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
from pydantic import BaseModel

# pydantic models
class ArticleBase(BaseModel):
    title: str
    description: str
    author: str
    
class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id:int
    class Config:
        orm_mode = True

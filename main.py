from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional,List
from sqlalchemy.orm import Session

# database 
from database import SessionLocal, engine, Base
from models import ArticleModel
Base.metadata.create_all(bind=engine)

# service import
from service import ArticleService

app = FastAPI(
    title='Article API',
    description='This project is aimed at demonstrating how to connect to a database(Relational) using FastAPI',
    version='1.0.0'
)


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


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def home():
    return {"message":"connecting to a relational database"}


@app.get('/articles',
status_code=200,
tags=['articles'],
summary='get all the articles', 
response_description='all articles',
response_model=List[Article]
)
async def get_articles(db: Session = Depends(get_db)):
    articels = ArticleService.get_articles(db=db)
    return {
        "articles":articels
    }


@app.get('/articles/{article_id}',
status_code=200,
tags=['articles'],
summary='get an article by its id', 
response_description='an article',
response_model = Article
)
async def get_article(article_id:int, db:Session = Depends(get_db)):
    the_article = ArticleService.get_article(db=db, article_id=article_id)
    if the_article is None:
        raise HTTPException(status_code=404, detail="The article does not exist")
    
    return the_article

@app.post('/posts',
status_code=201,
tags=['articles'],
summary='create a new articles', 
response_description='the created article',
response_model=Article
)
async def create_article(article:ArticleCreate, db: Session = Depends(get_db)):
    return ArticleService.create_new_article(db=db, article=article)



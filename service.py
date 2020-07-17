
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import ArticleModel
from schemas import ArticleCreate, Article

class ArticleService:

    @staticmethod
    def get_articles(db: Session):
        """"Get a list of all articles from the database"""
        return db.query(ArticleModel).all()

    @staticmethod
    def get_article(db:Session, article_id:int):
        """return an article that matches the id provided"""
        return db.query(ArticleModel).filter(ArticleModel.id==article_id).first()


    @staticmethod
    def create_new_article(db:Session, article:ArticleCreate):
        """Insert an article in the database"""
        the_article = ArticleModel(**article.dict())
        db.add(the_article)
        db.commit()
        # db.refresh(the_article)
        return the_article


    @staticmethod
    def update_article(db:Session, article_id:int,article:ArticleCreate):
        """update article details"""
        the_article:Article = db.query(ArticleModel).filter(ArticleModel.id==article_id).first()
        if the_article is None:
            raise HTTPException(status_code=404, detail="Artical not found")

        the_article.title = article.title
        the_article.description = article.description
        the_article.author = article.author
        db.commit()
        return the_article

    @staticmethod
    def delete_article(article_id:int,db:Session):
        the_article:Article = db.query(ArticleModel).filter(ArticleModel.id==article_id).first()
        if the_article is None:
            raise HTTPException(status_code=404, detail="Artical not found")
        
        db.delete(the_article)
        db.commit()

        return {"message":"article successfully deleted"}
        


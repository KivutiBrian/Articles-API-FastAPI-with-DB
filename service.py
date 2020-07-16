
from sqlalchemy.orm import Session
from models import ArticleModel

class ArticleService:

    @staticmethod
    def get_articles(db: Session):
        """"Get a list of all articles from the database"""
        return db.query(ArticleModel).all()

    @staticmethod
    def get_article(db:Session, article_id:int):
        return db.query(ArticleModel).filter(ArticleModel.id==article_id).first()


    @staticmethod
    def create_new_article(db:Session, article):
        """Insert an article in the database"""
        the_article = ArticleModel(**article.dict())
        db.add(the_article)
        db.commit()
        # db.refresh(the_article)
        return the_article



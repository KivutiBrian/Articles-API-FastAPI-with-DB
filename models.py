from database import Base
from sqlalchemy import Column, String, Integer


class ArticleModel(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    description = Column(String)
    author = Column(String)


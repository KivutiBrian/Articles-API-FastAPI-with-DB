from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database URI
SQLALCHEMY_DATABASE_URI = "sqlite:///article_app.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}, echo=False
)

""""
echo - shortcut to setup SQLAlchemy logging, which is accomplished via python standard logging
     - with it we can see all the generated SQL produced

return value of create_engine() is an instance of Engine, which represents the core interface to the database

connect_args is needed only for SQLite

"""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
To start talking to our database, the ORM's handle to the database is the Session

"""


Base = declarative_base()

"""
Using the Declarative system, we can create classes that include directives to describe the actual database table they will map to
A class using Declarative at a minimum needs a __tablename__ attribute and atleast one Column

"""

from sqlalchemy import create_engine
from app.utils.constants import DATABASE_URL
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(url=DATABASE_URL)
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

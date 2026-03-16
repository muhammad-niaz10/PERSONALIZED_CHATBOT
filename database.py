from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.core.config import DATABASE_URL

engine=create_engine(DATABASE_URL)

session = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()



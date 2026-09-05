from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Yields a database session, and guarantees it's closed afterward —
    even if the request raises an error partway through."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
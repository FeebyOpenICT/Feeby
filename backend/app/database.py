from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from config import POSTGRES_PASSWORD, POSTGRES_USER, DATABASE_URL

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DATABASE_URL}:5432/feeby"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db_connection() -> Session:
    """
    Dependency generator to create database connection for calls that require the connection

    returns a sqlalchemy.orm Session 
    """
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()

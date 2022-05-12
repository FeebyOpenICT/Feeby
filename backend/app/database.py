from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://feeby:hallo123@db:5432/feeby"

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

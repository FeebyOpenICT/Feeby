from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://feeby:hallo123@localhost:5432/feeby"

engine = create_engine(
  SQLALCHEMY_DATABASE_URL,
  echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db_connection():
  """
  Dependency to create database connection for calls that require the connection
  """
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

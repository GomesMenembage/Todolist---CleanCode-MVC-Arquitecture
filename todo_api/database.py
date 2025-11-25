from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///todo.db")

Base = declarative_base()

def start_database():
    Base.metadata.create_all(bind= db)

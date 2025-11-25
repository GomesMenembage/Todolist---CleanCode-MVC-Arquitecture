from database import db
from sqlalchemy.orm import sessionmaker

def create_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()
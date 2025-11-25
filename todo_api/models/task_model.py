from sqlalchemy import Column, String, Integer
from database import Base

class Tasks(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    
    title = Column(String, nullable = False)
    
    def __init__(self, title):
        self.title = title
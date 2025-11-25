from pydantic import BaseModel

class CreateTask(BaseModel):
    title: str
        
class ReadTask(BaseModel):
    id: int
    title: str
    
    class Config:
        orm_mode = True
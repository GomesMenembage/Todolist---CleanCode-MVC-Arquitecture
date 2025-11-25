from fastapi import FastAPI
from database import start_database

app = FastAPI()

from routes.task_router import todo
@app.on_event("startup")
async def startup():
    start_database()
    
    
app.include_router(todo)
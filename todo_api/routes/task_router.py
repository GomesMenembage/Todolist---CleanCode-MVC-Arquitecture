from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependences import create_session
from models.schemas import CreateTask, ReadTask
from controllers import tasks_controller

todo = APIRouter(prefix = "/tasks", tags=["TodoList"])

@todo.get("/",response_model = list[ReadTask])
async def get_all (session: Session = Depends(create_session)):
    return tasks_controller.get_all_tasks(session)
    
@todo.post("/create", response_model = ReadTask)
async def create_new_task(data: CreateTask,session: Session = Depends(create_session)):
    return tasks_controller.create_task(data, session)
    
@todo.delete("/{task_id}/delete", response_model = ReadTask)
async def delete_task(task_id:int, session: Session = Depends(create_session)):
    task_to_delete = tasks_controller.delete_task(session, task_id)
    if not task_to_delete:
        raise HTTPException(status_code = 404,detail = "task not found")
    return task_to_delete
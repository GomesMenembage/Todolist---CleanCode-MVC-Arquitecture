from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models.task_model import Tasks
from models.schemas import CreateTask
from dependences import create_session

def create_task(data: CreateTask, session: Session= Depends(create_session)):
    new_task = Tasks(title = data.title)
    session.add(new_task)
    session.commit()
    return new_task
    
def get_all_tasks(session: Session = Depends(create_session)):
        return session.query(Tasks).all()
        
def delete_task(session: Session = Depends(create_session), task_id = int):
    task_to_delete = session.query(Tasks).filter(Tasks.id == task_id).first()
    if task_to_delete is None:
        return None
    session.delete(task_to_delete)
    session.commit()
    
    return task_to_delete
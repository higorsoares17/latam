from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.tasks_model import Task


class TaskRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Task]:
        query = self.db.query(Task)
        return query.offset(start).limit(limit).all()
    
    def create(self, task:Task) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task
    

    def delete(self, task: Task) -> None:
        del_task = self.db.query(Task).filter_by(id=task.id).first()
        if not del_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_task)
        self.db.commit()
        self.db.flush()

    def update(self, task: Task) -> Task:
        self.db.merge(task)
        self.db.commit()
        return task
from models.tasks_model import Task
from fastapi import Depends
from typing import Optional, List
from schemas.task_schema import TaskSchema
from repositories.tasks_repository import TaskRepository   


class TaskService:
    task_repository: TaskRepository

    def __init__(
        self, task_repository: TaskRepository = Depends()
    ) -> None:
        self.task_repository = task_repository

    def list(
        self, 
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Task]:
        return self.task_repository.list(
            page_size, start_index
        )
    
    def create(self, task: TaskSchema) -> Task:
        return self.task_repository.create(
            Task(
                id = task.id,
                name = task.name,
                due_date = task.due_date,
                assignee= task.assignee,
                status = task.status,
                section = task.section,
                id_aplication = task.id_aplication,
            )
        )
    
    def delete(self, id: int) -> None:
        return self.task_repository.delete(Task(id=id))
    
    def update(self, task: TaskSchema) -> Task:
        return self.task_repository.update(
            Task(
                id = task.id,
                name = task.name,
                due_date = task.due_date,
                assignee= task.assignee,
                status = task.status,
                section = task.section,
                id_aplication = task.id_aplication,
            )
        )
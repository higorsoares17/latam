from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.task_schema import TaskSchema
from services.task_service import TaskService


TaskRouter = APIRouter(prefix="/v1/task", tags=["Task"])


@TaskRouter.get("/", response_model=List[TaskSchema])
def index(
    task_service: TaskService = Depends(),
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        task.normalize()
        for task in task_service.list(
            page_size, start_index
        )
    ]


@TaskRouter.post(
    "/",
    response_model=TaskSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    task: TaskSchema,
    task_service: TaskService = Depends(),
):
    return task_service.create(task)


@TaskRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, task_service: TaskService = Depends()):
    return task_service.delete(id)


@TaskRouter.put(
    "/",
    response_model=TaskSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    task: TaskSchema,
    task_service: TaskService = Depends()
):
    return task_service.update(task)

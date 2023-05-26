from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.assignee_schema import AssigneeSchema
from services.assignee_service import AssigneeService


AssigneeRouter = APIRouter(prefix="/v1/assignee", tags=["Assignee"])



@AssigneeRouter.get("/", response_model=List[AssigneeSchema])
def index(
    assignee_service: AssigneeService = Depends(),
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        user.normalize()
        for user in assignee_service.list(
            page_size, start_index
        )
    ]
    
@AssigneeRouter.post(
    "/",
    response_model=AssigneeSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    assignee: AssigneeSchema,
    assignee_service: AssigneeService = Depends(),
):
    return assignee_service.create(assignee)



@AssigneeRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, assignee_service: AssigneeService = Depends()):
    return assignee_service.delete(id)


@AssigneeRouter.put(
    "/",
    response_model=AssigneeSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    assignee: AssigneeSchema,
    assignee_service: AssigneeService = Depends()
):
    return assignee_service.update(assignee)

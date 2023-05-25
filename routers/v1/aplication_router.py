from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.aplication_schema import AplicationSchema
from services.aplication_service import AplicationService


AplicationRouter = APIRouter(prefix="/v1/aplication", tags=["Aplication"])



@AplicationRouter.get("/", response_model=List[AplicationSchema])
def index(
    aplication_service: AplicationService = Depends(),
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        aplication.normalize()
        for aplication in aplication_service.list(
            page_size, start_index
        )
    ]
    
@AplicationRouter.post(
    "/",
    response_model=AplicationSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    aplication : AplicationSchema,
    aplication_service: AplicationService = Depends(),
):
    return aplication_service.create(aplication)



@AplicationRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, aplication_service: AplicationService = Depends()):
    return aplication_service.delete(id)


@AplicationRouter.put(
    "/",
    response_model=AplicationSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    aplication: AplicationSchema,
    aplication_service: AplicationService = Depends()
):
    return aplication_service.update(aplication)

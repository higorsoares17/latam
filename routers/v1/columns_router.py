from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.column_schema import ColumnSchema, ColumnSchemaCreate
from services.column_service import ColumnService


ColumnRouter = APIRouter(prefix="/v1/column", tags=["Column"])



@ColumnRouter.get("/", response_model=List[ColumnSchema])
def index(
    column_service: ColumnService = Depends(),
    name: Optional[str] = None,
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        column.normalize()
        for column in column_service.list(
            name, page_size, start_index
        )
    ]
    
@ColumnRouter.post(
    "/",
    response_model=ColumnSchemaCreate,
    status_code=status.HTTP_201_CREATED
)
def create(
    card: ColumnSchemaCreate,
    column_service: ColumnService = Depends(),
):
    return column_service.create(card)



@ColumnRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, column_service: ColumnService = Depends()):
    return column_service.delete(id)


@ColumnRouter.put(
    "/",
    response_model=ColumnSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    card: ColumnSchema,
    column_service: ColumnService = Depends()
):
    return column_service.update(card)

from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.startup_schema import StartupSchema
from services.startup_service import StartupService


StartupRouter = APIRouter(prefix="/v1/startup", tags=["Startup"])



@StartupRouter.get("/", response_model=List[StartupSchema])
def index(
    startup_service: StartupService = Depends(),
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        startup.normalize()
        for startup in startup_service.list(
            page_size, start_index
        )
    ]
    
@StartupRouter.post(
    "/",
    response_model=StartupSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    startup: StartupSchema,
    startup_service: StartupService = Depends(),
):
    return startup_service.create(startup)



@StartupRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, startup_service: StartupService = Depends()):
    return startup_service.delete(id)


@StartupRouter.put(
    "/",
    response_model=StartupSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    startup: StartupSchema,
    startup_service: StartupService = Depends()
):
    return startup_service.update(startup)

from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.attachments_schema import AttachmentsSchema
from services.attachments_service import AttachemntsService


AttachmentsRouter = APIRouter(prefix="/v1/attachments", tags=["Attachments"])



@AttachmentsRouter.get("/", response_model=List[AttachmentsSchema])
def index(
    attachemnt_service: AttachemntsService = Depends(),
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        attachment.normalize()
        for attachment in attachemnt_service.list(
            page_size, start_index
        )
    ]
    
@AttachmentsRouter.post(
    "/",
    response_model=AttachmentsSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    attachment: AttachmentsSchema,
    attachemnt_service: AttachemntsService = Depends(),
):
    return attachemnt_service.create(attachment)



@AttachmentsRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, attachemnt_service: AttachemntsService = Depends()):
    return attachemnt_service.delete(id)


@AttachmentsRouter.put(
    "/",
    response_model=AttachmentsSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    attachment: AttachmentsSchema,
    attachemnt_service: AttachemntsService = Depends()
):
    return attachemnt_service.update(attachment)

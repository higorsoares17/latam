from models.attachments_model import Attachments
from fastapi import Depends
from typing import Optional, List
from schemas.attachments_schema import AttachmentsSchema
from repositories.attachments_repository import AttachmentsRepository


class AttachemntsService:
    attachments_repository: AttachmentsRepository

    def __init__(
        self, attachments_repository: AttachmentsRepository = Depends()
    ) -> None:
        self.attachments_repository = attachments_repository

    def list(
        self, 
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Attachments]:
        return self.attachments_repository.list(
            page_size, start_index
        )
    
    def create(self, attachments: AttachmentsSchema) -> Attachments:
        return self.attachments_repository.create(
            Attachments(
                id = attachments.id,
                filename = attachments.filename,
                full_path = attachments.full_path,
                id_aplication = attachments.id_aplication,
            )
        )
    
    def delete(self, id: int) -> None:
        return self.attachments_repository.delete(Attachments(id=id))
    
    def update(self, attachments: AttachmentsSchema) -> Attachments:
        return self.attachments_repository.update(
            Attachments(
                id = attachments.id,
                filename = attachments.filename,
                full_path = attachments.full_path,
                id_aplication = attachments.id_aplication,
            )
        )

       
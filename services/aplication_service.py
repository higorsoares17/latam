from models.aplication_model import Aplication
from fastapi import Depends
from typing import Optional, List
from schemas.aplication_schema import AplicationSchema,AplicationSchemaUpdate
from repositories.aplication_repository import AplicationRepository



class AplicationService:
    aplication_repository: AplicationRepository

    def __init__(
        self, aplication_repository: AplicationRepository = Depends()
    ) -> None:
        self.aplication_repository = aplication_repository

    def list(
        self,
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Aplication]:
        return self.aplication_repository.list(
            page_size, start_index
        )
    
    def create(self, aplication: AplicationSchema) -> Aplication:
        return self.aplication_repository.create(
            Aplication(aplication)
        )
    
    def create(self, aplication: AplicationSchema) -> Aplication:
        return self.aplication_repository.create(
            Aplication(
                id_card = aplication.id_card,
                due_date = aplication.due_date,
                score = aplication.score
            )
        )
    
    def delete(self, id: int) -> None:
        return self.aplication_repository.delete(Aplication(id=id))
    
    def update(self, aplication: AplicationSchemaUpdate) -> Aplication:
        return self.aplication_repository.update(Aplication(id=aplication.id))
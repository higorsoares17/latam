from models.column_model import Columns
from fastapi import Depends
from typing import Optional, List
from schemas.column_schema import ColumnSchema
from repositories.column_repository import ColumnRepository


class ColumnService:
    column_repository: ColumnRepository

    def __init__(
        self, column_repository: ColumnRepository = Depends()
    ) -> None:
        self.column_repository = column_repository

    def list(
        self,
        name: Optional[str] = None,
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Columns]:
        return self.column_repository.list(
            name, page_size, start_index
        )
    
    def create(self, column: ColumnSchema) -> Columns:
        return self.column_repository.create(
            Columns(name=column.name)
        )
    
    def delete(self, id: int) -> None:
        return self.column_repository.delete(Columns(id=id))
    
    def update(self, column: ColumnSchema) -> Columns:
        return self.column_repository.update(Columns(name=column.name, id=column.id))
from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.column_model import Columns


class ColumnRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Columns]:
        query = self.db.query(Columns)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()
    
    def create(self, column:Columns) -> Columns:
        self.db.add(column)
        self.db.commit()
        self.db.refresh(column)
        return column
    

    def delete(self, column: Columns) -> None:
        del_column = self.db.query(Columns).filter_by(id=column.id).first()
        if not del_column:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_column)
        self.db.commit()
        self.db.flush()

    def update(self, column: Columns) -> Columns:
        self.db.merge(column)
        self.db.commit()
        return column
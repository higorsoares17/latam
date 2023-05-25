from typing import List, Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.aplication_model import Aplication


class AplicationRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Aplication]:
        query = self.db.query(Aplication)
        return query.offset(start).limit(limit).all()
    
    def create(self, aplication:Aplication) -> Aplication:
        self.db.add(aplication)
        self.db.commit()
        self.db.refresh(aplication)
        return aplication
    

    def delete(self, aplication: Aplication) -> None:
        del_aplication = self.db.query(Aplication).filter_by(id=aplication.id).first()
        if not del_aplication:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_aplication)
        self.db.commit()
        self.db.flush()

    def update(self, aplication: Aplication) -> Aplication:
        self.db.merge(aplication)
        self.db.commit()
        return aplication
from typing import List, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.card_model import Card
from models.column_model import Column


class CardRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Card]:
        query = self.db.query(Card)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()

    def create(self, card:Card) -> Card:
        crt_card = self.db.query(Column).filter(id=card.id_column).first()
        if not crt_card:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id Column não encontrado")
        
        self.db.add(card)
        self.db.commit()
        self.db.refresh(card)
        return card

    def delete(self, card: Card) -> None:
        del_card = self.db.query(Card).filter_by(id=card.id).first()
        if not del_card:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        self.db.delete(del_card)
        self.db.commit()
        self.db.flush()

    def update(self, card: Card) -> Card:
        self.db.merge(card)
        self.db.commit()
        return card
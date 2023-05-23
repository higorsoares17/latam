from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.card_model import Card


class CardRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)) -> None:
        self.db = db

    def create(self, card:Card) -> Card:
        self.db.add(card)
        self.db.commit()
        self.db.refresh(card)
        return card


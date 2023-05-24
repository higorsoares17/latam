from models.card_model import Card
from fastapi import Depends
from typing import Optional, List
from schemas.card_schema import CardSchema, CardSchemaCreate, CardSchemaUpdate
from repositories.card_repository import CardRepository


class CardService:
    card_repository: CardRepository

    def __init__(
        self, card_repository: CardRepository = Depends()
    ) -> None:
        self.card_repository = card_repository

    def list(
        self,
        name: Optional[str] = None,
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Card]:
        return self.card_repository.list(
            name, page_size, start_index
        )

    def create(self, card: CardSchemaCreate) -> Card:
        return self.card_repository.create(
            Card(name=card.name, id_column=card.id_column)
        )
    
    def delete(self, id: int) -> None:
        return self.card_repository.delete(Card(id=id))
    
    def update(self, card: CardSchemaUpdate) -> Card:
        return self.card_repository.update(Card(name=card.name, id=card.id, id_column=card.id_column))
    
    
from models.card_model import Card
from fastapi import Depends
from schemas.card_schema import CardSchema
from repositories.card_repository import CardRepository


class CardService:
    card_repository: CardRepository

    def __init__(
        self, card_repository: CardRepository = Depends()
    ) -> None:
        self.card_repository = card_repository

    def create(self, card: CardSchema) -> Card:
        return self.card_repository.create(
            Card(name=card.name)
        )

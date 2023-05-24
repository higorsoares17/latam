from fastapi import APIRouter, Depends, status
from schemas.card_schema import (
    CardSchema,
    CardSchemaCreate
)
from services.card_service import CardService
from typing import List, Optional
CardRouter = APIRouter(prefix="/v1/cards", tags=["Cards"])


@CardRouter.get("/", response_model=List[CardSchema])
def index(
    card_service: CardService = Depends(),
    name: Optional[str] = None,
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        card.normalize()
        for card in card_service.list(
            name, page_size, start_index
        )
    ]
    
@CardRouter.post(
    "/",
    response_model=CardSchemaCreate,
    status_code=status.HTTP_201_CREATED
)
def create(
    card: CardSchemaCreate,
    card_service: CardService = Depends(),
):
    return card_service.create(card)


@CardRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, card_service: CardService = Depends()):
    return card_service.delete(id)


@CardRouter.put(
    "/",
    response_model=CardSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    card: CardSchema,
    card_service: CardService = Depends()
):
    return card_service.update(card)

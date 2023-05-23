from fastapi import APIRouter, Depends, status
from schemas.card_schema import CardSchema
from services.card_service import CardService
from typing import List, Optional


CardRouter = APIRouter(prefix="/v1/cards", tags=["cards"])


@CardRouter.post(
    "/", 
    response_model=CardSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    card: CardSchema,
    card_service: CardService = Depends(),
):
    return card_service.create(card)
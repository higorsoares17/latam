from fastapi import APIRouter, Depends, status
from typing import List, Optional
from schemas.challenge_schema import ChallengeSchema
from services.challenge_service import ChallengeService


ChallengeRouter = APIRouter(prefix="/v1/challenge", tags=["Challenge"])


@ChallengeRouter.get("/", response_model=List[ChallengeSchema])
def index(
    challenge_service: ChallengeService = Depends(),
    page_size: Optional[int] = 100,
    start_index: Optional[int] = 0,
):
    return [
        challenge.normalize()
        for challenge in challenge_service.list(
            page_size, start_index
        )
    ]


@ChallengeRouter.post(
    "/",
    response_model=ChallengeSchema,
    status_code=status.HTTP_201_CREATED
)
def create(
    challenge: ChallengeSchema,
    challenge_service: ChallengeService = Depends(),
):
    return challenge_service.create(challenge)


@ChallengeRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, challenge_service: ChallengeService = Depends()):
    return challenge_service.delete(id)


@ChallengeRouter.put(
    "/",
    response_model=ChallengeSchema,
    status_code=status.HTTP_202_ACCEPTED
)
def update(
    challenge: ChallengeSchema,
    challenge_service: ChallengeService = Depends()
):
    return challenge_service.update(challenge)

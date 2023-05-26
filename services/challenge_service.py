from models.challenge_model import Challenge
from fastapi import Depends
from typing import Optional, List
from schemas.challenge_schema import ChallengeSchema
from repositories.challenge_repository import ChallengeRepository


class ChallengeService:
    challenge_repository: ChallengeRepository

    def __init__(
        self, challenge_repository: ChallengeRepository = Depends()
    ) -> None:
        self.challenge_repository = challenge_repository

    def list(
        self, 
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Challenge]:
        return self.challenge_repository.list(
            page_size, start_index
        )
    
    def create(self, challenge: ChallengeSchema) -> Challenge:
        return self.challenge_repository.create(
            Challenge(
                id = challenge.id,
                desafio = challenge.desafio,
                id_aplication = challenge.id_aplication
            )
        )
    
    def delete(self, id: int) -> None:
        return self.challenge_repository.delete(Challenge(id=id))
    
    def update(self, challenge: ChallengeSchema) -> Challenge:
        return self.challenge_repository.update(
            Challenge(
                id = challenge.id,
                desafio = challenge.desafio,
                id_aplication = challenge.id_aplication
            )
        )
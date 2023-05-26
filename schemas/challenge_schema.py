from pydantic import BaseModel
from typing import Optional

class ChallengeSchema(BaseModel):
    id: Optional[int]
    desafio: str
    id_aplication : int
    
    class Config:
        orm_mode = True

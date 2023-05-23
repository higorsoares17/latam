from pydantic import BaseModel
from typing import Optional


class CardSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True
        
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class AplicationSchemaUpdate(BaseModel):
    id: int
    score: float
    due_date: datetime
    id_card : int


class AplicationSchema(BaseModel):
    score: float
    due_date: datetime
    id_card : int

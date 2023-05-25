from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class AplicationSchemaDelete(BaseModel):
    id: int


class AplicationSchema(BaseModel):
    startup: Optional[List]
    score: float
    due_date: datetime
    id_card = int

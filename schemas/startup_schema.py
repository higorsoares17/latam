from pydantic import BaseModel
from typing import Optional

class StartupSchema(BaseModel):
    id: Optional[int]
    name: str
    id_aplication : int

    class Config:
        orm_mode = True



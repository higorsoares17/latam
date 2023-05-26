from pydantic import BaseModel
from typing import Optional

class AttachmentsSchema(BaseModel):
    id: Optional[int]
    filename : str
    full_path : str
    id_aplication : int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional

class CommentsSchema(BaseModel):
    id: Optional[int]
    comentario : str
    id_user : int
    id_aplication : int

    class Config:
        orm_mode = True

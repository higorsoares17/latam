from pydantic import BaseModel
from typing import Optional

class AssigneeSchema(BaseModel):
    id: Optional[int]
    email: str
    name : str
    id_aplication : int
    id_user : int
    
    class Config:
        orm_mode = True

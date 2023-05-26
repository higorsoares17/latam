from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int]
    user: str
    password : str
    admin : bool
    
    class Config:
        orm_mode = True


class UserSchemaUpdate(BaseModel):
    id: Optional[int]
    user: str
    password : str
    
    class Config:
        orm_mode = True


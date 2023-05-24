from pydantic import BaseModel
from typing import Optional

class ColumnSchema(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True

class ColumnSchemaCreate(BaseModel):
    name: str
    
    class Config:
        orm_mode = True

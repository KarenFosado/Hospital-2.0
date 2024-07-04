from typing import List, Union
from pydantic import BaseModel 
from datetime import datetime

class userBase(BaseModel):
    usuario: str
    password: str
    created_at: datetime
    estatus: bool 
    Id_PERSONA: int
    
class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int 
    
    class Config: 
        orm_mode = True
from typing import List, Union
from pydantic import BaseModel 
from datetime import datetime

class userBase(BaseModel):
    usuario: str
    password: str
    created_at: datetime
    estatus: bool 
    Id_persona: int
    
class UserCreate(userBase):
    pass

class UserUpdate(userBase):
    pass


class User(userBase):
    id: int 
    
    class Config: 
        from_attributes = True
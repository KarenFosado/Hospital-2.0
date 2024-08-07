from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class OrganoBase(BaseModel):
    Nombre: str
    Descripcion: str
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class OrganoCreate(OrganoBase):
    pass

class OrganoUpdate(OrganoBase):
    pass

class Organo(OrganoBase):
    ID: int
    class Config:
        orm_mode = True

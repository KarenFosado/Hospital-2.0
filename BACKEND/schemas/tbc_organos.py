from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class AparatoSistemaEnum(str, Enum):
    Circulatorio = 'Circulatorio'
    Digestivo = 'Digestivo'
    Respiratorio = 'Respiratorio'
    Nervioso = 'Nervioso'
    Muscular = 'Muscular'
    Esqueletico = 'Esquelético'
    Endocrino = 'Endocrino'
    Linfatico = 'Linfático'
    Inmunologico = 'Inmunológico'
    Reproductor = 'Reproductor'
    Urinario = 'Urinario'
    Sensorial = 'Sensorial'

class DisponibilidadEnum(str, Enum):
    Disponible = 'Disponible'
    NoDisponible = 'No Disponible'
    Reservado = 'Reservado'

class TipoEnum(str, Enum):
    Vital = 'Vital'
    NoVital = 'No Vital'

class OrganoBase(BaseModel):
    Nombre: str
    Aparato_Sistema: AparatoSistemaEnum
    Descripcion: str
    Disponibilidad: DisponibilidadEnum
    Tipo: TipoEnum
    Estatus: bool

# Esquema para crear un órgano, no incluye las fechas
class OrganoCreate(OrganoBase):
    pass

# Esquema para actualizar un órgano, tampoco incluye las fechas
class OrganoUpdate(OrganoBase):
    pass

# Esquema para la respuesta, incluye las fechas
class Organo(OrganoBase):
    ID: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

    class Config:
        orm_mode = True

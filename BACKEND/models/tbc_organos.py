from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from config.db import Base

class Organo(Base):
    __tablename__ = "tbc_organos"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(60))
    Descripcion = Column(String(200))
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)

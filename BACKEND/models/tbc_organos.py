from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Text
from sqlalchemy.sql import func
from config.db import Base

class Organo(Base):
    __tablename__ = "tbc_organos"

    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(45), nullable=False)
    Aparato_Sistema = Column(Enum('Circulatorio', 'Digestivo', 'Respiratorio', 'Nervioso', 'Muscular', 'Esquelético', 'Endocrino', 'Linfático', 'Inmunológico', 'Reproductor', 'Urinario', 'Sensorial'), nullable=False)
    Descripcion = Column(Text, nullable=False)
    Disponibilidad = Column(Enum('Disponible', 'No Disponible', 'Reservado'), nullable=False)
    Tipo = Column(Enum('Vital', 'No Vital'), nullable=False)
    Fecha_Actualizacion = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    Fecha_Registro = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    Estatus = Column(Boolean, default=True)

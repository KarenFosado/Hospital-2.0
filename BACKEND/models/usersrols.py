from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship 
ftom config.db import Base
import models.users , models.rols


class UserRol(Base): 
    __tablename__ = "tbd_usarios_roles"
    
    Usuario_ID = Column(Integer, ForeignKey("tbb_usarios.ID"), primary_key= True)
    Rol_ID = Column (Integer, ForeignKey("tbc_roles.ID"), primary_key= True)
    Estatus= Column(Boolean)
    Fecha_Registro = Column(Datetime)
    Fecha_Actualizacion = Column(DateTime)
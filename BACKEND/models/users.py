from sqlalchemy import Column, Integer, String, Boolean, Datetime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base 

class User(Base):
    __tablename__ = "users"
    
    id= Column(Integer, primary_key=True, index=True)
    usuario= Column(String(255))
    password = column(LONGTEXT)
    created_at = Column(Datetime)
    estatus = Column(Boolean, default=False)
    Id_persona = Column(Integer)
    
    #itsem = relationship("Item", back_populates="owner") Clave foranea

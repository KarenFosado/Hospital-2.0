from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

persona = APIRouter()
personas = []

class ModelPersona(BaseModel):
    id: int
    nombre: str
    primer_apellido: str
    segundo_apellido: Optional[str]
    edad: int
    fecha_nacimiento: datetime
    curp: str
    tipo_sangre: str
    created_at: datetime = datetime.now()
    status: bool = False

class UpdatePersona(BaseModel):
    nombre: Optional[str]
    primer_apellido: Optional[str]
    segundo_apellido: Optional[str]
    edad: Optional[int]
    fecha_nacimiento: Optional[datetime]
    curp: Optional[str]
    tipo_sangre: Optional[str]
    status: Optional[bool]

# Ruta para obtener todas las personas
@persona.get("/persona", response_model=List[ModelPersona])
async def get_personas():
    """
    Obtiene la lista de todas las personas.
    """
    return personas

# Ruta para guardar una nueva persona
@persona.post("/persona")
async def save_personas(datos_persona: ModelPersona):
    """
    Guarda una nueva persona en la lista.
    """
    personas.append(datos_persona)
    return 'Datos Guardados'

# Ruta para actualizar una persona existente
@persona.put("/persona/{persona_id}")
async def update_persona(persona_id: int, datos_actualizados: UpdatePersona):
    """
    Actualiza los datos de una persona existente.
    """
    for idx, persona in enumerate(personas):
        if persona.id == persona_id:
            update_data = datos_actualizados.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(personas[idx], key, value)
            return 'Datos Actualizados'
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Ruta para eliminar una persona existente
@persona.delete("/persona/{persona_id}")
async def delete_persona(persona_id: int):
    """
    Elimina una persona de la lista.
    """
    for idx, persona in enumerate(personas):
        if persona.id == persona_id:
            del personas[idx]
            return 'Datos Eliminados'
    raise HTTPException(status_code=404, detail="Persona no encontrada")

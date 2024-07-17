from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import crud.users, config.db, schemas.users, models.users
from typing import List
from jwt_config import solicita_token
from portadortoken import portador

user = APIRouter()

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@user.post("/login/", response_model=schemas.users.UserLogin, tags=["User Login"])
def read_credentials(usuario:schemas.users.UserLogin, db: Session = Depends(get_db)):
    db_credentials = crud.users.get_user_by_credentials(db, username=usuario.Nombre_Usuario, correo=usuario.Correo_electronico, telefono=usuario.Numero_Telefonico_Movil, password=usuario.Contrasena )
    if db_credentials is None: 
        return JSONResponse(content={'mensaje':'Acceso denegado'},status_code=404)
    token:str=solicita_token(usuario.dict())
    return JSONResponse(status_code=200, content=token)
    

@user.get("/users/", response_model=List[schemas.users.User], tags=["Users"], dependencies=[Depends(portador())])
def read_users(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    db_users = crud.users.get_users(db=db, skip=skip, limit=limit)
    return db_users

@user.get("/users/{id}", response_model=schemas.users.User, tags=["Users"], dependencies=[Depends(portador())])
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/users/", response_model=schemas.users.User, tags=["Users"])
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.users.get_user_by_usuario(db=db, usuario=user.Nombre_Usuario)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario existente, intenta nuevamente más tarde...")
    return crud.users.create_user(db=db, user=user)

@user.put("/users/{id}", response_model=schemas.users.User, tags=["Users"], dependencies=[Depends(portador())])
def update_user(id: int, user: schemas.users.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.users.update_user(db=db, id=id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado, no fue actualizado")
    return db_user

@user.delete("/users/{id}", response_model=schemas.users.User, tags=["Users"], dependencies=[Depends(portador())])
def delete_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.users.delete_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado, no se pudo eliminar")
    return db_user

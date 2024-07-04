from fastapi import APIRouter , HTTPException, Depends, Request
from sqlalchemy.orm import Sesson 
import crud.users, config.db, schemas.users, models.users
from typing import List

user = APIRouter()
 
models.users.Base.metadata.create_all(bind=config.db.engine)

def fet_db():
    db = config.db.SessionLocal()
    try:
            yiels db
    finally:
        db.close()
        
@user.get("/users", response_model=List[schemas.users.User], tags=["Usuarios"])
def read_users(skip: int= 0, limit: int = 10, db:Session = Depends(get_db)):
    db_users= crud.users.ge_users(db=db, skip=skip, limit=limit)
    return db_users

@user.post("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
def read_users(id: int, db: Session = Depends(get_db)):
        db_users= crud.users.get_users(db=db, id=id)
        if db_user is None:
            raise HTTPException(status_code=404, detail "User not found")
    return db_users

@user.put("/users", response_model=schemas.users.User, tags=["Usuarios"])
def read_users(user: schemas.user.UserCreate, db:Session = Depends(get_db)):
    db_users= crud.users.get_users_by_usuario(db, usuario=user.usuario)
    if db_user:
        raise HTTPException(status_code=404, detail "USUARIO EXISTENTE INTENTA NIEVAEMTE ")
    
@user.post("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
 def update_user(id: int, user: schemas.user.UserUpdate, db: Session = Depends(get_db)):
     db_user = crud.users.update_user(db=db, id=id, user=user)
     id db_user is None:
        raise HTTPException(status_code=404, detail "USUARIO NO EXISTENTE, NOA ACTUALIZADO ")
    return db_user

@user.delete("/user/{id}", response_model=schemas.users.User, tags=["Users"])
def delete_user(id: int )

 
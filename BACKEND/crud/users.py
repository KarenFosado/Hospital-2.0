import models.users
import schemas.users
import sqlalchemy.orm import Session


def get_user(sb: Session, id: int):
    retur db.query(models.User.User).filter(models.User.User.id == id).first()
    
def get_user_by_usuario(db: Session, usuario: str):
    return db.query(models.User.User).filter(models.User.User.usuario == usuario).first()

def get_users(db: Session, skip: int = 0, limit: int = 10)
    return db.query(models.User.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.users.UserCreate):
    db_users = models.users.User(usuario=user.usuario, password=user.password, create_at=user.creted)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.user.User).filter(models.users.User.id == id).first()
    id db_user:
        for var , value in vars(user).items():
            setatr(br_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(sb: Session, id: int):
    db_user = db.query(models.user.User).filter(models.users.User.id == id).first()
    id db_user:
        db.delete(db_user)
        db.commit()
    return db_user
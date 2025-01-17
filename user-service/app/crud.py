from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from . import models, schemas, auth

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    print("---------------------> users ", user)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        tenant_id=user.tenant_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    data = db.query(models.User).filter(models.User.email == email).first()
    print("user data----------------->", data)
    return data
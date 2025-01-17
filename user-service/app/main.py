from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud, auth
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

import requests

def validate_tenant_id(tenant_id: int):
    response = requests.get(f"http://tenant-service:8001/tenants/{tenant_id}/exists")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid tenant_id")
       
@app.post("/users/register")
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    validate_tenant_id(user.tenant_id)
    db_user = crud.get_user_by_email(db, email=user.email)
    
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    data = crud.create_user(db=db, user=user)
    # res = schemas.UserCreate(**data.__dict__)
    # res = {
    #     "name" : data.username,
    #     "email" : data.email,
    #     "tenant_id" : data.tenant_id
    # }
    return data

@app.post("/users/login", response_model=schemas.Token)
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = auth.create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
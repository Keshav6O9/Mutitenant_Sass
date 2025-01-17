from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

models.Base.metadata.create_all(bind=engine)
from typing import List
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@app.post("/tenants/")
def create_tenant(tenant:schemas.TenantCreate, db:Session = Depends(get_db)):
   
    db_tenant =  crud.get_tenant_by_email(db, email=tenant.email)
    if db_tenant:
        raise HTTPException(status_code=400, detail="Email Already Registerd")
    data = crud.create_tenanat(db=db, tenant=tenant)

    data = schemas.TenantCreate(**data.__dict__)
    data = {
        "name" : data.name,
        "email" : data.email,
        "plan" : data.plan
    }

    return data
   
    

@app.get("/tenants/{tenant_id}", response_model = schemas.Tenant)
def read_tenant(tenant_id: int, db:Session = Depends(get_db)):
    db_tenant = crud.get_tenant(db, tenant_id=tenant_id)
    if db_tenant is None:
        raise HTTPException(status_code=400, detail="Tenant not found")
    return JSONResponse(content=jsonable_encoder(db_tenant))

@app.get("/tenants/", response_model=List[schemas.Tenant])
def read_tenants(skip: int=0, limit:int=100, db:Session= Depends(get_db)):
    tenants = crud.get_tenants(db, skip=skip, limit=limit)
    for i in tenants:
        print(i.email)
    return JSONResponse(content=jsonable_encoder(tenants))
    
    
@app.get("/tenants/{tenant_id}/exists")
def check_tenant_exists(tenant_id: int, db: Session = Depends(get_db)):
    tenant = crud.get_tenant(db, tenant_id=tenant_id)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return {"exists": True}
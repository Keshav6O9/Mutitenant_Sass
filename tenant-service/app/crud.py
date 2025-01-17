from sqlalchemy.orm import Session
from . import models, schemas

def create_tenanat(db:Session, tenant: schemas.TenantCreate):
    db_tenant = models.Tenant(**tenant.dict())
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    
    print("db tenteant---------------->", db_tenant)
    print("schema----------------------",schemas.TenantCreate(**db_tenant.__dict__))
    return db_tenant
    # return schemas.TenantCreate(**db_tenant.__dict__)


def get_tenant(db:Session, tenant_id:int):
    return db.query(models.Tenant).filter(models.Tenant.id == tenant_id).first()

def get_tenant_by_email(db:Session, email:str):
    return db.query(models.Tenant).filter(models.Tenant.email == email).first()
import json
def get_tenants(db:Session, skip:int = 0, limit:int=100):
    data = db.query(models.Tenant).offset(skip).limit(limit).all()
    print("get data -------------------->",data)
    return data
""" 
Define pydantic Schema for tenants
"""


from pydantic import BaseModel

class TenantCreate(BaseModel):
    name:str
    email:str
    plan:str
    
    class Config:
        orm_mode = True
    
class Tenant(BaseModel):
    id:int
    name:str
    email:str
    plan:str
    is_active:bool = True
    
    class Config:
        from_attributes = True
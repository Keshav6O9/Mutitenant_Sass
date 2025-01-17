from pydantic import BaseModel , EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    tenant_id: int

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    tenant_id: int
    is_active: bool
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
"""
Database model for tenanat
"""

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Tenant(Base):
    __tablename__ = "tenants"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email =  Column(String, unique=True, index=True)
    plan= Column(String, default="free")
    is_active = Column(Boolean, default=True)
    
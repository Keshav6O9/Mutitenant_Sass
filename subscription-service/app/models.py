from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base

class Subscription(Base):
    __tablename__ = "subscriptions"
    
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer)
    pan = Column(String,nullable=False)
    status = Column(String, nullable=False, default="active")
    
    stripe_customer_id = Column(String, unique=True)
    stripe_subscription_id = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
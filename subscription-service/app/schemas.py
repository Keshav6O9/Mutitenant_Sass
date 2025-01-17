from pydantic import BaseModel
from datetime import datetime

class SubscriptionCreate(BaseModel):
    tenant_id: int
    plan : str
    stripe_customer_id : str
    stripe_subscription_id: str
    
class Subscription(BaseModel):
    id: int
    tenant_id : int
    plan: str
    status: str
    stripe_customer_id: str
    stripe_subscription_id: str
    created_at: datetime
    updated_at:datetime
    
    class Config:
        from_attributes = True
        
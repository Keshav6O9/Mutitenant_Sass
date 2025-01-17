from sqlalchemy.orm import Session
from . import models, schemas

def create_subscription(db:Session, subscription: schemas.SubscriptionCreate):
    db_subscription = models.Subscription(**subscription.__dict__)
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

def get_subscription_by_tenant_id(db: Session, tenant_id: int):
    return db.query(models.Subscription).filter(models.Subscription.tenant_id == tenant_id).first()
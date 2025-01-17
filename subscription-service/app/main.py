from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, stripe_integration
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/subscriptions/", response_model=schemas.Subscription)
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = Depends(get_db)):
    # Create Stripe customer and subscription
    stripe_customer_id = stripe_integration.create_stripe_customer(email="tenant@example.com")
    stripe_subscription_id = stripe_integration.create_stripe_subscription(stripe_customer_id, subscription.plan)

    # Save subscription to database
    subscription.stripe_customer_id = stripe_customer_id
    subscription.stripe_subscription_id = stripe_subscription_id
    return crud.create_subscription(db=db, subscription=subscription)

@app.get("/subscriptions/{tenant_id}", response_model=schemas.Subscription)
def get_subscription(tenant_id: int, db: Session = Depends(get_db)):
    subscription = crud.get_subscription_by_tenant_id(db, tenant_id=tenant_id)
    if not subscription:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription
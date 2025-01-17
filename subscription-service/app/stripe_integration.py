import stripe 
from .config import settings

def create_stripe_customer(email:str):
    customer = stripe.Customer.create(email=email)
    return customer.id

def create_Stripe_subscription(customer_id:str, plan_id:str):
    subscription = stripe.Subscription.create(
        customer = customer_id,
        items =[{'price':plan_id}]
    )
    return subscription.id
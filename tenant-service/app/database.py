'''
Establishes the database connection
'''


from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings        

# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
SQLALCHEMY_DATABASE_URL="postgresql://tenant_Db_owner:6ngX1vSWtPDG@ep-super-rice-a5ow1ttu.us-east-2.aws.neon.tech/tenant_Db?sslmode=require"
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# metadata_obj = MetaData(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
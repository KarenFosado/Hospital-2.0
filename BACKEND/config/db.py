from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123@localhost:3307/test"
engine = create_engine(SQLALCHEMY_DATABASES_URL)
SessionLocal = sessionmaker(autocomit=false, autoflush=False, bind=engine)
Base= declarative_base()





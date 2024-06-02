from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace 'sqlite:///./test.db' with your database connection string
SQLALCHEMY_DATABASE_URL = "mongodb://admin:79e0c45cbf8d31f4@localhost:27017/startup"

# Create a SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session class using sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# from motor.motor_asyncio import AsyncIOMotorClient
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.future import select
# from sqlalchemy import Column, Integer, String

# # SQLAlchemy setup
# SQLALCHEMY_DATABASE_URL = "mongodb://admin:79e0c45cbf8d31f4@localhost:27017/startup"
# engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
# async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# Base = declarative_base()

# # MongoDB setup
# client = AsyncIOMotorClient(SQLALCHEMY_DATABASE_URL)
# db = client["startup"]
# collection = db["todo"]
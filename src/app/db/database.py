#app/db/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy_utils import database_exists, create_database, drop_database

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Environment variable to choose the database. Set this to 'postgres' or 'mysql'
DATABASE_TYPE = os.getenv('DATABASE_TYPE', 'postgres')

# Configuration for your database connections
DATABASE_URLS = {
    'mysql': "mysql+pymysql://root:Alvin%402016@localhost/workplan_maanager",
    'postgres': "postgresql+psycopg2://postgres:Aldmin123@localhost/workplan_manager"
}

# Select the appropriate database URL based on the DATABASE_TYPE
DATABASE_URL = DATABASE_URLS[DATABASE_TYPE]

ENGINE_OPTIONS = {"echo": True}

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, **ENGINE_OPTIONS)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

     
# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to reset the database (drop if exists and create)
def reset_database():
    if database_exists(engine.url):
        drop_database(engine.url)
    create_database(engine.url)

def create_tables():
    Base.metadata.create_all(bind=engine)
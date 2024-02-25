from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base import Base

DATABASE_URL = 'sqlite:///db/database.db'
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
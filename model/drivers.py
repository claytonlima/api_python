from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, CHAR, text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.db import SQLALCHEMY_DATABASE_URI
from datetime import datetime

Base = declarative_base()

class drivers(Base):
    __tablename__ = 'drivers'

    driver_id = Column('driver_id', Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', Integer)
    sex = Column('sex', CHAR)
    own_vehicle = Column('own_vehicle', CHAR)
    type_driver_license = Column('type_driver_license', CHAR)
    vehicle_loaded = Column('vehicle_loaded', CHAR)
    type_vehicle = Column('type_vehicle', Integer)
    created_data = Column('created_data', DateTime, default=datetime.now())
    updated_data = Column('updated_data', DateTime, default=datetime.now(),  onupdate=datetime.now())

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)




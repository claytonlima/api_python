from sqlalchemy import create_engine, Column, Integer, String, CHAR, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.db import SQLALCHEMY_DATABASE_URI
from datetime import datetime

Base = declarative_base()

class Drivers(Base):
    __tablename__ = 'drivers'

    driver_id = Column('driver_id', Integer, primary_key=True)
    name = Column('name', String)
    age = Column('age', Integer)
    sex = Column('sex', CHAR)
    own_vehicle = Column('own_vehicle', CHAR)
    type_driver_license = Column('type_driver_license', CHAR)
    vehicle_loaded = Column('vehicle_loaded', CHAR)
    type_vehicle = Column('type_vehicle', Integer)
    origin_latitude = Column('origin_latitude', String)
    origin_longitude = Column('origin_longitude', String)
    destiny_latitude = Column('destiny_latitude', String)
    destiny_longitude = Column('destiny_longitude', String)
    created_data = Column('created_data', DateTime, default=datetime.now())
    updated_data = Column('updated_data', DateTime, default=datetime.now(),  onupdate=datetime.now())

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


def insert_drivers_auto():
    session = Session()

    objects = [
        Drivers(driver_id=1, name='João Silva', age=25, sex='M', own_vehicle='S', type_driver_license='C', vehicle_loaded='S', type_vehicle=1, origin_latitude='-23.4585103', origin_longitude='-46.7668096', destiny_latitude='-23.7306369', destiny_longitude='-46.546628', created_data=datetime.now()),
        Drivers(driver_id=2, name='Pedro Cavalcante', age=27, sex='M', own_vehicle='S', type_driver_license='E', vehicle_loaded='N', type_vehicle=3, origin_latitude='-23.4585103', origin_longitude='-46.7668096', destiny_latitude='-23.7306369', destiny_longitude = '-46.546628', created_data=datetime.now()),
        Drivers(driver_id=3, name='Paulo Frias', age=30, sex='M', own_vehicle='S', type_driver_license='C', vehicle_loaded='S', type_vehicle=2, origin_latitude='-23.4585103', origin_longitude='-46.7668096', destiny_latitude='-23.7306369', destiny_longitude='-46.546628', created_data=datetime.now()),
        Drivers(driver_id=4, name='Judas Mariano', age=69, sex='M', own_vehicle='N', type_driver_license='E', vehicle_loaded='N', type_vehicle=5, origin_latitude='-23.4585103', origin_longitude='-46.7668096', destiny_latitude='-23.7306369', destiny_longitude='-46.546628', created_data=datetime.now()),
        Drivers(driver_id=5, name='Bezerra da Silva', age=50, sex='M', own_vehicle='S', type_driver_license='C', vehicle_loaded='S', type_vehicle=4, origin_latitude='-23.4585103', origin_longitude='-46.7668096', destiny_latitude='-23.7306369', destiny_longitude='-46.546628', created_data=datetime.now()),
     ]

    result = session.bulk_save_objects(objects)
    session.commit()
    session.close()

    return result

def get_driver(id):
    session = Session()
    result = session.query(Drivers).get(id)
    session.close()

    return result

def get_all_drivers():
    session = Session()
    stmt = text('SELECT driver_id, name, origin_latitude, origin_longitude, destiny_latitude, destiny_longitude  FROM drivers')
    stmt = stmt.columns(Drivers.driver_id, Drivers.name, Drivers.origin_latitude, Drivers.origin_longitude, Drivers.destiny_latitude, Drivers.destiny_longitude)
    drivers_information = session.query(Drivers).from_statement(stmt).all()
    session.close()

    drivers = []
    for driver_information in drivers_information:
        drivers.append({
            'driver_id': driver_information.driver_id,
            'name': driver_information.name,
            'origin_latitude': driver_information.origin_latitude,
            'origin_longitude': driver_information.origin_longitude,
            'destiny_latitude': driver_information.destiny_latitude,
            'destiny_longitude': driver_information.destiny_longitude,
        })

    return drivers




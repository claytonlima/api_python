from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import *

Base = declarative_base()

class TrucksTypes(Base):
    __tablename__ = "trucks_types"

    truck_id = Column('truck_id', Integer, primary_key=True)
    truck_name = Column('truck_name', String)
    created_data = Column('created_data', TIMESTAMP)
    updated_data = Column('updated_data', TIMESTAMP)


engine = create_engine('sqlite:///project_trucks', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

# session = Session()
# new_truck_type = TrucksTypes()
# new_truck_type.truck_id = 9
# new_truck_type.truck_name = 'Optimus Prime'
# new_truck_type.created_data = datetime.now()
# new_truck_type.updated_data = datetime.now()
#
# session.add(new_truck_type)
# session.commit()
# session.close()
#
# session = Session()
# trucks_types = session.query(TrucksTypes).all()
#
# for truck_type in trucks_types:
#     print(truck_type.truck_id)
#     print(truck_type.truck_name)
#
# session.close()


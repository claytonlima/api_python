from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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


def list_all_trucks():
    session = Session()
    stmt = text('SELECT truck_id, truck_name FROM trucks_types')
    stmt = stmt.columns(TrucksTypes.truck_id, TrucksTypes.truck_name)
    trucks_types = session.query(TrucksTypes).from_statement(stmt).all()
    session.close()

    trucks = []
    for truck_type in trucks_types:
        trucks.append({
            'truck_id': truck_type.truck_id,
            'truck_name': truck_type.truck_name
        })

    return trucks


def add(truck_name, criado_em, atualizado_em):
    session = Session()
    new_truck_type = TrucksTypes()
    new_truck_type.truck_name = truck_name
    new_truck_type.created_data = criado_em
    new_truck_type.updated_data = atualizado_em

    result = session.add(new_truck_type)
    session.commit()
    session.close()

    return result

def update(type_id, truck, criado_em, atualizado_em):
    session = Session()
    result = session.query(TrucksTypes) \
        .filter(TrucksTypes.truck_id == type_id) \
        .update({
        TrucksTypes.truck_name: truck,
        TrucksTypes.updated_data: atualizado_em
    })

    session.commit()
    session.close()

    if result == 1:
        return 200

def delete(id):
    session = Session()
    result = session.query(TrucksTypes).filter(TrucksTypes.truck_id == id).delete()
    session.commit()
    session.close()

    if result == 1:
        return 200

    return result
from bottle import run, get, post, delete, route, request, template
from db import uri_conrection
from datetime import datetime
from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, VARCHAR, DateTime)

engine = create_engine(uri_conrection, encoding='utf-8', echo=True)

metadata = MetaData(bind=engine)

table_drivers = Table('drivers', metadata,
                   Column('driver_id', Integer, primary_key=True),
                   Column('nome', VARCHAR(40)),
                   Column('idade', Integer),
                   Column('sexo', VARCHAR(1)),
                   Column('veiculo_proprio', VARCHAR(1)),
                   Column('tipo_cnh', VARCHAR(1)),
                   Column('carregado', VARCHAR(1)),
                   Column('veiculo_tipo', Integer),
                   Column('criado_em', DateTime, default=datetime.now),
                   Column('atualizado_em', DateTime, default=datetime.now, onupdate=datetime.now)
                   )

metadata.create_all()


table_types_of_trucks = Table('types_of_trucks', metadata,
                   Column('type_id', Integer, primary_key=True),
                   Column('truck', VARCHAR(40), index=True),
                   Column('criado_em', DateTime, default=datetime.now),
                   Column('atualizado_em', DateTime, default=datetime.now, onupdate=datetime.now)
                   )

metadata.create_all()



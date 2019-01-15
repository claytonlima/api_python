import jinja2
from bottle import route, run, request
from truck_types import Session, TrucksTypes
from sqlalchemy import *
from datetime import datetime

def get_template(template):
    templateLoader = jinja2.FileSystemLoader(searchpath="./views")
    templateEnv = jinja2.Environment(loader=templateLoader)
    template    = templateEnv.get_template(template)
    return template.render()

@route('/')
def index():
    template = 'index.html'
    return get_template(template)


@route('/alltypesoftrucks')
def getAll():
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

    return {'results': trucks}

@route('/typeoftruck/edit/:id', method='PUT')
def update_type_of_truck(id):
    type_id = id
    truck = request.params.get('truck')
    criado_em = datetime.now()
    atualizado_em = datetime.now()

    session = Session()
    result = session.query(TrucksTypes)\
        .filter(TrucksTypes.truck_id == type_id)\
        .update({
        TrucksTypes.truck_name: truck,
        TrucksTypes.created_data: criado_em,
        TrucksTypes.updated_data: atualizado_em
    })

    session.commit()
    session.close()

    return {'result': result}

run(port=8080)
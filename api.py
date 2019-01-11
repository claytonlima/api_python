import jinja2
from bottle import route, run, request
from sqlalchemy import *
from table import table_types_of_trucks
import json
import datetime

def get_template(template):
    templateLoader = jinja2.FileSystemLoader(searchpath="./views")
    templateEnv    = jinja2.Environment(loader=templateLoader)
    template       = templateEnv.get_template(template)
    return template.render()

@route('/')
def index():
    template = 'index.html'
    return get_template(template)

@route('/alltypesoftrucks')
def getAll():
    s = select([table_types_of_trucks.c.type_id,
                table_types_of_trucks.c.truck
              ])

    res = s.execute()
    
    return json.dumps([dict(r) for r in res])

@route('/typeoftruck/edit/:id', method='PUT')
def update_type_of_truck(id):
    type_id       = id
    truck         = request.params.get('truck')
    criado_em     = datetime.datetime.now()
    atualizado_em = datetime.datetime.now()

    s = table_types_of_trucks.update().values({
        table_types_of_trucks.c.truck: truck,
        table_types_of_trucks.c.criado_em : criado_em,
        table_types_of_trucks.c.atualizado_em: atualizado_em,
    }).where(table_types_of_trucks.c.type_id == type_id)

    s = s.execute();
    return print(s)

run(port=8181)
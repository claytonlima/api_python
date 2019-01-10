from bottle import jinja2_view, route, run, request
from sqlalchemy import select
from table import table_types_of_trucks
import json

@route('/<cadastro>')
@jinja2_view('views/cadastro.html')
def cadastro(cadastro):
    return dict(nome=cadastro)

@route('/alltypesoftrucks')
def getAll():
    s = select([table_types_of_trucks.c.type_id,
                table_types_of_trucks.c.truck
              ])

    res = s.execute()
    
    return json.dumps([dict(r) for r in res])

run(port=8080)
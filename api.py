import jinja2
from bottle import route, run, request
from jinja2 import *
from sqlalchemy import select
from table import table_types_of_trucks
import json

def get_template(template):
    templateLoader = jinja2.FileSystemLoader(searchpath="./views")
    templateEnv    = jinja2.Environment(loader=templateLoader)
    template       = templateEnv.get_template(template)
    return template

@route('/')
def index():
    template = 'index.html'
    template = get_template(template)
    return template.render()

@route('/alltypesoftrucks')
def getAll():
    s = select([table_types_of_trucks.c.type_id,
                table_types_of_trucks.c.truck
              ])

    res = s.execute()
    
    return json.dumps([dict(r) for r in res])

run(port=8082)
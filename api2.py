import jinja2
from bottle import route, run
from truck_types import Session, TrucksTypes
from sqlalchemy import text

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

run(port=8080)
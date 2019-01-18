from bottle import route, run, request
from truck_types import add, update, delete, list_all_trucks
from datetime import datetime


@route('/alltypesoftrucks')
def getAll():
    result = list_all_trucks()

    return {'results': result}

@route('/typeoftruck/add', method='POST')
def add_new_type_of_truck():
    truck_name = request.params.get('truck')
    criado_em = datetime.now()
    atualizado_em = datetime.now()

    result = add(truck_name, criado_em, atualizado_em)

    return {'result': result}

@route('/typeoftruck/edit/:id', method='PUT')
def update_type_of_truck(id):
    type_id = id
    truck = request.params.get('truck')
    atualizado_em = datetime.now()

    result = update(type_id, truck, atualizado_em)

    return {'result': result}

@route('/typeoftruck/del/:id', method='DELETE')
def remove_type_of_truck(id):
    result = delete(id)
    return {'result': result}

run(port=8080)
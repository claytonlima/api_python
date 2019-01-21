from bottle import route, run, request
from model.truck_types import add, update, delete, insert_types_of_trucks_auto, list_all_trucks
from model.drivers import insert_drivers_auto, get_driver, get_all_drivers, get_all_drivers_vehicle_loaded, get_all_drivers_vehicle_not_loaded, get_all_drivers_own_vehicle, get_all_drivers_not_own_vehicle, get_all_drivers_origin_destiny_group_type
from lib.geocoding_functions import get_origin_destiny_latitude_longitude
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

@route('/typeoftruck/addMock', method='POST')
def insert_mock_type_of_trucks():
    result = insert_types_of_trucks_auto()

    return {'result': result}


@route('/typeoftruck/del/:id', method='DELETE')
def remove_type_of_truck(id):
    result = delete(id)
    return {'result': result}

## EndPoints from drivers

@route('/driver/list/:id', method='GET')
def list_driver(id):
    result = get_driver(id)

    result_origin_driver = get_origin_destiny_latitude_longitude(result.origin_latitude,  result.origin_longitude)
    result_destiny_driver = get_origin_destiny_latitude_longitude(result.destiny_latitude, result.destiny_longitude)

    return {'result':
           [
             {
                 'driver_id': result.driver_id,
                 'driver_name': result.name,
                 'origin': result_origin_driver,
                 'destiny': result_destiny_driver
             }
            ]
            }

@route('/driver/addMock', method='POST')
def add_drivers_auto():
    result = insert_drivers_auto()

    return {'result': result}

@route('/driver/listalldrivers', method='GET')
def list_driver_all_with_origin_destiny():
    drivers = get_all_drivers()

    drivers_origin_destiny = []
    for driver in drivers:
        result_origin_driver = get_origin_destiny_latitude_longitude(driver['origin_latitude'], driver['origin_longitude'])
        result_destiny_driver = get_origin_destiny_latitude_longitude(driver['destiny_latitude'], driver['destiny_longitude'])
        drivers_origin_destiny.append({'driver_id': driver['driver_id'], 'driver_name': driver['name'], 'origin': result_origin_driver, 'destiny': result_destiny_driver})
    drivers_origin_destiny

    return {'result': drivers_origin_destiny}

@route('/driver/vehicleloaded', method='GET')
def list_drivers_vehicle_loaded():
    drivers_vehicle_loaded = get_all_drivers_vehicle_loaded()

    return {'result': drivers_vehicle_loaded}

@route('/driver/vehiclenotloaded', method='GET')
def list_drivers_vehicle_not_loaded():
    drivers_vehicle_not_loaded = get_all_drivers_vehicle_not_loaded()

    return {'result': drivers_vehicle_not_loaded}

@route('/driver/vehiclenotloaded', method='GET')
def list_drivers_vehicle_not_loaded():
    drivers_vehicle_not_loaded = get_all_drivers_vehicle_not_loaded()

    return {'result': drivers_vehicle_not_loaded}

@route('/driver/ownvehicle', method='GET')
def list_drivers_own_vehicle():
    drivers_vehicle_own_vehicle = get_all_drivers_own_vehicle()

    return {'result': drivers_vehicle_own_vehicle}

@route('/driver/notownvehicle', method='GET')
def list_drivers_not_own_vehicle():
    drivers_vehicle_not_own_vehicle = get_all_drivers_not_own_vehicle()

    return {'result': drivers_vehicle_not_own_vehicle}

@route('/driver/alldriversorigindestinygrouptype', method='GET')
def list_drivers_origin_destiny_group_type():
    all_drivers_origin_destiny_group_type = get_all_drivers_origin_destiny_group_type()

    origin_destiny_type = []
    for all_driver_origin_destiny_group_type in all_drivers_origin_destiny_group_type:
        result_origin_driver_type = get_origin_destiny_latitude_longitude(all_driver_origin_destiny_group_type['origin_latitude'], all_driver_origin_destiny_group_type['origin_longitude'])
        result_destiny_driver_type = get_origin_destiny_latitude_longitude(all_driver_origin_destiny_group_type['destiny_latitude'], all_driver_origin_destiny_group_type['destiny_longitude'])
        origin_destiny_type.append({'origin': result_origin_driver_type, 'destiny': result_destiny_driver_type})

    return {'result': origin_destiny_type}

    return {'result': all_drivers_origin_destiny_group_type}

run(port=8080)
from table import table_types_of_trucks, engine

conn = engine.connect()

ins = table_types_of_trucks.insert()

conn.execute(table_types_of_trucks.insert(), [
    {'type_id': 1, 'truck': 'Caminhão 3/4'},
    {'type_id': 2, 'truck': 'Caminhão Toco'},
    {'type_id': 3, 'truck': 'Caminhão Truck'},
    {'type_id': 4, 'truck': 'Carreta Simples'},
    {'type_id': 5, 'truck': 'Carreta Eixo Extendido'},
])



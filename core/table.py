from bottle import run, get, post, delete, route, request, template
from db import uri_conrection
from datetime import datetime
from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, VARCHAR, DateTime)

engine = create_engine(uri_conrection, encoding='latin1', echo=True)

metadata = MetaData(bind=engine)

table_usuarios = Table('usuarios', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('nome', VARCHAR(40), index=True),
                   Column('idade', Integer, nullable=False),
                   Column('senha', VARCHAR(40)),
                   Column('criado_em', DateTime, default=datetime.now),
                   Column('atualizado_em', DateTime, default=datetime.now, onupdate=datetime.now)
                   )

metadata.create_all()

# animals = [
#     {'name': 'Ellie', 'type': 'Elephant'},
#     {'name': 'Python', 'type': 'Snake'},
#     {'name': 'Zed', 'type': 'Zebra'}
# ]


# @app.get('/')
# def show(db):
#     table_data = db.query(TheTable)
#
#     results = []
#
#     for x in table_data:
#         results.append({'name': x.name})
#     return {'table_data': results}

# app.run(debug=True, reloader=True)
# @get('/animal')
# def getAll():
#     return {'animals': animals}
#
# @get('/animal/<name>')
# def getOne(name):
#     the_animal = [animal for animal in animals if animal['name'] == name]
#     return {'animal': the_animal[0]}
#
# @post('/animal')
# def addOne():
#     new_animal = {'name': request.json.get('name'), 'type': request.json.get('type')}
#     animals.append(new_animal)
#     return {'animals': animals}
#
# @delete('/animal/<name>')
# def removeOne(name):
#     the_animal = [animal for animal in animals if animal['name'] == name]
#     animals.remove(the_animal[0])
#     return {'animals': animals}
#
# @route('/')
# def index():
#     return template('index')
#
# @route('/jsonData')
# def jsonData():
#     return {"name": "Clayton", "myList": [1,2,3,4,5]}

# if __name__ == '__main__':
#     run(debug=True, reloader=True)
from table import table_usuarios, engine

conn = engine.connect()

ins = table_usuarios.insert()

conn.execute(table_usuarios.insert(), [
    {'nome': 'Marivaldo', 'idade': 35, 'senha': 'gatinho_123'},
    {'nome': 'jean', 'idade': 18, 'senha': 'jeanzinho_123'},
    {'nome': 'Juacir', 'idade': 27, 'senha': 'juacinho_123'}
])



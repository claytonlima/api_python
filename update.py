from sqlalchemy import update
from table import table_usuarios, engine

conn = engine.connect()

u = update(table_usuarios).where(table_usuarios.c.nome == 'Juacir')

u = u.values(nome='Juacy')

result = conn.execute(u)

print(result.rowcount)

conn.close()
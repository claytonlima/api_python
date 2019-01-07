from sqlalchemy import select
from table import table_usuarios


s = select([table_usuarios])

for row in s.execute():
    print(row)


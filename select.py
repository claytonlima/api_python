from sqlalchemy import select
from table import table_types_of_trucks

def all_types_of_trucks():
    s = select([table_types_of_trucks.c.type_id,
                table_types_of_trucks.c.truck
              ])

    types_trucks=[]

    for row in s.execute():
        types_trucks.append(row)
    return types_trucks

import sqlalchemy as sa

engine = sa.create_engine("sqlite:///hr.db")
connection = engine.connect()

meta_data = sa.MetaData()

employees = sa.Table('Employees', meta_data, autoload_with=engine)
query = sa.select([employees])
result = connection.execute(query)
result_set = result.fetchall()
print(result_set[:3])

query1 = sa.select([employees]).where(employees.column.position == 'Software engineer')
print(query1)

query2 = employees.select()
print(new_query)

# UPDATE
update_query = employees.update().where(employees.c.id==1).values(position='Instructor')
connection.execute(update_query)

# table.update().where(conditions).values(SET expression)
# e.g. Employees.update().where(Emp_ID == 1).values(name='Erik')

# DELETE
delete_query = employees.delete().where(employees.c.id==1)
print(delete_query)


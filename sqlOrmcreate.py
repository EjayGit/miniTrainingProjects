from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///hr.db')
Base = declarative_base()

class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()
#row1 = Employees(name='Erik', position='AGI manufacturer')
#session.add(row1)
"""session.add_all([Employees(name='Renaud', position='Software Engineer'),
                Employees(name='Dave', position='Cyber Sec'),
                Employees(name='Steve', position='AGI engineer')])
session.commit()"""
#query = session.query(Employees).all()
# query = session.query(Employees).get(3)
# query = session.query(Employees).filter(Employees.id == 3) # or '!= 3'
# query = session.query(Employees).filter(Employees.name.like('%e%'))
#for employee in query:
#    print('Name', employee.name, 'Position', employee.position)

query = session.query(Employees).get(1)
query.update({Employees.name: 'Mr Erik Clark'})
session.commit()
#print(query.name, query.position)
#query.name = 'Erik Clark'
#session.commit()
#query = session.query(Employees).get(1)
#print(query.name, query.position)
#session.delete(query)
# src/models/employee.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

Base = declarative_base()

f = Faker ()

# An instance for Faker
fake = Faker (locale='en_US')

# Function for employees
def create_employees(num_employees):
#an empty list to add emloyees dictionaries
 employee_list =[]

#employees dictionary
 for i in range(1,num_employees):
  employee = {}
  employee = {'first_name': fake.first_name()}
  employee = {'last_name': fake.last_name()}
  employee = {'job' : fake.job ()}
  employee = {'department': fake.random_elements(elements= ('IT','HR', 'Marketing', 'Finance'))}
  employee = {'role' : fake.random_elements(elements= ('Manager', 'Analyst', 'Developer','Associate'))}
  employee = {'salary' : fake.random_int(min=30000, max=150000, step=1000)}
  employee_list.append(employee)
  return pd.dataframe 

print(create_employees(7))



class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    job = Column(String)
    department = Column(String)

    def __init__(self, id, firstname, lastname,job, department):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.job = job
        self.department =department

    def __repr__(self):
        return f"<Employee(id={self.id}, firstname={self.firstname}, lastname={self.lastname})>"

# Connect to the database
#engine = create_engine('mysql+mysqlconnector://root:Kaltuma@89@127.0.0.1:3306/testdb', echo=True)

# Create the session
#Session = sessionmaker(bind=engine)
#session = Session()

# Create Employee instances
#employee1 = Employee(2972, "James", "Maina")
#employee2 = Employee(3056, "John", "Doe")
#employee3 = Employee(4829, "Jane", "Maina")
#employee4 = Employee(5721, "Tom", "Baker")

# Add employees to the session and commit changes
#session.add_all([employee1, employee2, employee3, employee4])
#session.commit()

            
##myDB.gen_table(1001,fields=['name','city','phone','company','job_title','email'],
               #Name your file 
               #db_file='eDB022.db',
               #Name your table
               #table_name='users',
#rimarykey='name',real_city=True)
   
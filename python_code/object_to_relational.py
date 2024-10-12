#  Date & Time 27/07/2024, 06:58.
#  @author Mesfin Haftu

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Person(Base):
	__tablename__ = "people"
	ssn = Column("ssn", Integer, primary_key=True, unique=True)
	first_name = Column("first_name", String)
	last_name = Column("last_name", String)
	gender = Column("gender", String)
	age = Column("age", Integer)

	def __init__(self, ssn, first_name, last_name, gender, age):
		self.ssn = ssn
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.age = age

	def __repr__(self):
		return f"({self.ssn}) {self.first_name} {self.last_name} ({self.gender}) {self.age}"

class Things(Base):
	__tablename__ = "things"
  
	tid = Column("tid", Integer, primary_key=True, unique=True)
	name = Column("name", String)
	owner = Column("owner", Integer, ForeignKey("people.ssn"))

	def __init__(self, tid, name, owner):
		self.tid = tid
		self.name = name
		self.owner = owner

	def __repr__(self):
		return f"({self.tid}) {self.name} owned by {self.owner}"

engine = create_engine("sqlite:///mydb.db", echo=True) # creates a database engine
Base.metadata.create_all(bind=engine)  # creates all classes into the database

Session =sessionmaker(bind=engine) # creates a session for the database
session = Session()

# person = Person(12345, "Mesfin", "Haftu", "m", 30)
# p1 = Person(12321, "Bob", "Blue", "m", 35)
# p2 = Person(34543, "Anna", "Blue", "f", 40)
# p3 = Person(45654, "Angela", "Cold", "f", 22)

# session.add(person)
# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()

# t1 = Things(1, "MacBook", person.ssn)
# t2 = Things(2, "Phone", p2.ssn)
# t3 = Things(3, "Home", p3.ssn)
# t4 = Things(4, "Pickup", person.ssn)

# session.add(t1)
# session.add(t2)
# session.add(t3)
# session.add(t4)
# session.commit()



# results = session.query(Person).filter(Person.last_name == "Blue")
# results = session.query(Person).filter(Person.age > 30)
# results = session.query(Person).filter(Person.first_name.like("%An%"))
# results = session.query(Person).filter(Person.first_name.in_(["Anna", "Mesfin"])) # filter by multiple values
results = session.query(Person, Things).filter(Person.ssn == Things.owner).filter(Person.first_name == "Mesfin") # filter by multiple values

for result in results:
	print(result)

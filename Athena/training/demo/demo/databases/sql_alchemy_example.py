from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String
 
#############################################################################
# Set up a database "engine" that links to a database and populate it with
# data.
#############################################################################

engine = create_engine('sqlite:///tutorial.db',
                       echo=True)
 
metadata = MetaData(bind=engine)
 
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(40)),
              Column('age', Integer),
              Column('password', String),
              )
 
addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )
 
# create tables in database
# You can call it as often as you like. It always check for the existence 
# of the specified table before trying to create it.
metadata.create_all()

#############################################################################
# Connecting to an existing table.
#############################################################################
users_again = Table("users", metadata, autoload=True)

#############################################################################
# Inserting with a connection
#############################################################################

# create an Insert object
ins = users.insert()
# add values to the Insert object
new_user = ins.values(name="Joe", age=20, password="pass")
 
# create a database connection
conn = engine.connect()
# add user to database by executing SQL
conn.execute(new_user)

#############################################################################
# Insert without a connection object.
#############################################################################

# a connectionless way to Insert a user
ins = users.insert()
result = engine.execute(ins, name="Shinji", age=15, password="nihongo")
 
# another connectionless Insert
result = users.insert().execute(name="Martha", age=45, password="dingbat")

#############################################################################
# Insert multiple items into a table..
#############################################################################
conn.execute(addresses.insert(), [ 
    {'user_id': 1, 'email_address' : 'jack@yahoo.com'},
    {'user_id': 1, 'email_address' : 'jack@msn.com'},
    {'user_id': 2, 'email_address' : 'www@www.org'},
    {'user_id': 2, 'email_address' : 'wendy@aol.com'},
])

#############################################################################
# Select all from a table.
#############################################################################

from sqlalchemy.sql import select
 
# Select all values from users
s = select([users])
result = s.execute()
 
print 'All Users (one by one):'
for row in result:
    print row
print

#############################################################################
# Select all from a table into a list of tuples.
#############################################################################

conn = engine.connect()
res = conn.execute(s)
rows = res.fetchall()    

print 'All Users (in a list):'
print rows
print

#############################################################################
# Select just the names and the ages from the user table.
#############################################################################

s = select([users.c.name, users.c.age])
result = conn.execute(s)  

print 'User names and ages:'
for row in result:  
    print row
print

#############################################################################
# Select Cartesian product of tables (not so useful)...
#############################################################################
 
s = select([users, addresses])
result = s.execute()
 
print 'Cartesian product of tables:'
for row in result:
    print row
print

#############################################################################
# Combining tables with rows that have matching IDs.
#############################################################################
s = select([users, addresses], users.c.id==addresses.c.user_id)
result = s.execute()
 
print 'Users and Addresses:'
for row in result:
    print row
print

#############################################################################
# Using the "and" operator in selection.
#############################################################################
from sqlalchemy.sql import and_, or_, not_
s = select([users, addresses], and_(users.c.id==addresses.c.user_id,
                                    users.c.age>15)   
          )
result = s.execute()
 
print 'Users and Addresses:'
for row in result:
    print row
print


#############################################################################
# Using join.
#############################################################################

user_address_join = users.join(addresses)
print 'SQL Join Statement:', user_address_join

s = select([users.c.name, addresses.c.email_address], from_obj=user_address_join)
result = s.execute()
 
print 'Users and Addresses:'
for row in result:
    print row
print


#############################################################################
#############################################################################
# The ORM
#############################################################################
#############################################################################

#############################################################################
# Defining a class to map to the database.
#############################################################################

class User(object): 

    def __init__(self, name, age, password): 
        self.name = name 
        self.age = age 
        self.password = password 

    def __repr__(self): 
        return "<User('%s','%i', '%s')>" % (self.name, self.age, self.password) 

user = User("Joe", 23, "foo")
print 'user:', user

#############################################################################
# Mapping the class to a table in the db.
#############################################################################

from sqlalchemy.orm import mapper 

mapper(User, users) 
ed_user = User('Ed', 24, 'edspassword') 
print "Ed's id:", str(ed_user.id) 

#############################################################################
# Adding users through a session.
#############################################################################
from sqlalchemy.orm import sessionmaker 
Session = sessionmaker(bind=engine) 

session = Session()

session.add_all([ 
  User('Wendy', 20, 'foobar'), 
  User('Mary', 30, 'xxg527'), 
  User('Fred', 40, 'blah')]) 

session.commit()


#############################################################################
# Querying a session.
#############################################################################
for instance in session.query(User).order_by(User.name): 
    print instance.name, instance.age 

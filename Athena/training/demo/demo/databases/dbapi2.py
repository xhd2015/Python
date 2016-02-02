
# This could be any DB-API 2.0 compliant database
#  Although some change in the connect arguments may be necessary
#  For example --- adding user= and password= keywords
import sqlite3 as db

database = ':memory:'
#database = '/tmp/mydata'
conn = db.connect(database)

c = conn.cursor()

sql = """create table stocks
(date text, trans text, symbol text, 
qty real, price real)"""
c.execute(sql)

sql = """insert into stocks
         values ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)"""
c.execute(sql)

conn.commit()

stocks = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
          ('2006-04-05', 'BUY', 'MSOFT', 1000, 72.00),
          ('2006-04-06', 'SELL', 'IBM', 500, 53.00)]
sql = "insert into stocks values (?,?,?,?,?)"
for t in stocks:
    c.execute(sql, t)

t = ('IBM',)
c.execute('select * from stocks where symbol=?', t)

results = c.fetchall()
print results
del c
conn.close()

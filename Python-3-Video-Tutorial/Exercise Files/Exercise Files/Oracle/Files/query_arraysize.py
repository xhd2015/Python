import time
import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@orcl')

start = time.time()

cur = con.cursor()
cur.arraysize = 100
cur.execute('select * from bigtab')
res = cur.fetchall()
# print res  # uncomment to display the query results

elapsed = (time.time() - start)
print (elapsed, "seconds")

cur.close()
con.close()

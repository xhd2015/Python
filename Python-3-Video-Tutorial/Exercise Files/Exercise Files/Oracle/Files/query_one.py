import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@orcl')

cur = con.cursor()
cur.execute('select * from departments order by department_id')
row = cur.fetchone()
print (row)
row = cur.fetchone()
print (row)

cur.close()
con.close()

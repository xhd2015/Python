import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@orcl')

cur = con.cursor()
res = cur.callfunc('myfunc', cx_Oracle.NUMBER, ('abc', 2))
print (res)

cur.close()
con.close()

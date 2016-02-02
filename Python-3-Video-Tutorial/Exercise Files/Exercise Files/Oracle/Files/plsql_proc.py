import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@orcl')

cur = con.cursor()
myvar = cur.var(cx_Oracle.NUMBER)
cur.callproc('myproc', (123, myvar))
print (myvar.getvalue())

cur.close()
con.close()

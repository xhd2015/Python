import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@orcl')
print (con.version)

con.close()

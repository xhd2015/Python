import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@orcl')

rows = [ (1, "First" ),
         (2, "Second" ),
         (3, "Third" ),
         (4, "Fourth" ),
         (5, "Fifth" ),
         (6, "Sixth" ),
         (7, "Seventh" ) ]

cur = con.cursor()
cur.bindarraysize = 7
cur.setinputsizes(int, 20)
cur.executemany("insert into mytab(id, data) values (:1, :2)", rows)

# This is uncommented in the next step
#con.commit()

# Now query the results back

cur2 = con.cursor()
cur2.execute('select * from mytab')
res = cur2.fetchall()
print (res)
print(type(res))

cur.close()
cur2.close()
con.close()

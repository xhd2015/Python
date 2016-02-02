import cx_Oracle

con = cx_Oracle.connect('pythonhol', 'welcome', 'orcl', 
                        cclass = "PYTHONHOL", purity = cx_Oracle.ATTR_PURITY_SELF) 

print (con.version)

con.close()

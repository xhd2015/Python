import cx_Oracle


def main():
    try:
        con = cx_Oracle.connect('pythonhol/welcome@orcl')
        
        cur = con.cursor()
        cur.prepare('select * from departments where department_id = :id')
        
        cur.execute(None, {'id': 210})
        res = cur.fetchall()
        print (res)
        
        cur.execute(None, {'id': 110})
        res = cur.fetchall()
        print (res)
        
        cur.close()
        con.close()
    except cx_Oracle.DatabaseError as e:
        print(e)
        raise
if __name__ == "__main__": 
    main()
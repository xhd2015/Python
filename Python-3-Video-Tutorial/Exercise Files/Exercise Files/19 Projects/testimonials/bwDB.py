#!/usr/bin/python3
# bwTL - BW's template library
# by Bill Weinman [http://bw.org/]
# Copyright 1995-2010 The BearHeart Group LLC

import sqlite3

__version__ = '1.0.3'

class bwDB:
    def __init__(self, **kwargs):
        '''
            db = bwDB( [ table = ''] [, filename = ''] )
            constructor method
                table is for CRUD methods 
                filename is for connecting to the database file
        '''
        # see filename setter below
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', '')

    def sql_do(self, sql, params = ()):
        '''
            db.sql_do( sql[, params] )
            method for non-select queries
                sql is string containing SQL
                params is list containing parameters
            returns nothing
        '''
        self._db.execute(sql, params)
        self._db.commit()

    def sql_query(self, sql, params = ()):
        '''
            db.sql_query( sql[, params] )
            generator method for queries
                sql is string containing SQL
                params is list containing parameters
            returns a generator with one row per iteration
            each row is a Row factory
        '''
        c = self._db.cursor()
        c.execute(sql, params)
        for r in c:
            yield r

    def sql_query_row(self, sql, params = ()):
        '''
            db.sql_query_row( sql[, params] )
            query for a single row
                sql is string containing SQL
                params is list containing parameters
            returns a single row as a Row factory
        '''
        c = self._db.cursor()
        c.execute(sql, params)
        return c.fetchone()

    def sql_query_value(self, sql, params = ()):
        '''
            db.sql_query_row( sql[, params] )
            query for a single value
                sql is string containing SQL
                params is list containing parameters
            returns a single value
        '''
        c = self._db.cursor()
        c.execute(sql, params)
        return c.fetchone()[0]

    def getrec(self, id):
        ''' 
            db.getrec(id)
            get a single row, by id
        '''
        query = 'SELECT * FROM {} WHERE id = ?'.format(self.table)
        c = self._db.execute(query, (id,))
        return c.fetchone()

    def getrecs(self):
        ''' 
            db.getrecs(id)
            get all rows, returns a generator of Row factories
        '''
        query = 'SELECT * FROM {}'.format(self.table)
        c = self._db.execute(query)
        for r in c:
            yield r

    def insert(self, rec):
        '''
            db.insert(rec)
            insert a single record into the table
                rec is a dict with key/value pairs corresponding to table schema
            omit id column to let SQLite generate it
        '''
        klist = sorted(rec.keys())
        values = [ rec[v] for v in klist ]  # a list of values ordered by key
        q = 'INSERT INTO {} ({}) VALUES ({})'.format(
            self.table,
            ', '.join(klist),
            ', '.join('?' for i in range(len(values)))
        )
        c = self._db.execute(q, values)
        self._db.commit()
        return c.lastrowid

    def update(self, id, rec):
        '''
            db.update(id, rec)
            update a row in the table
                id is the value of the id column for the row to be updated
                rec is a dict with key/value pairs corresponding to table schema
        '''
        klist = sorted(rec.keys())
        values = [ rec[v] for v in klist ]  # a list of values ordered by key

        for i, k in enumerate(klist):       # don't udpate id
            if k == 'id':
                del klist[i]
                del values[i]

        q = 'UPDATE {} SET {} WHERE id = ?'.format(
            self.table,
            ',  '.join(map(lambda str: '{} = ?'.format(str), klist))
        )
        self._db.execute(q, values + [ id ])
        self._db.commit()

    def delete(self, id):
        '''
            db.delete(id)
            delete a row from the table, by id
        '''
        query = 'DELETE FROM {} WHERE id = ?'.format(self.table)
        self._db.execute(query, [id])
        self._db.commit()

    def countrecs(self):
        '''
            db.countrecs()
            count the records in the table
            returns a single integer value
        '''
        query = 'SELECT COUNT(*) FROM {}'.format(self.table)
        c = self._db.cursor()
        c.execute(query)
        return c.fetchone()[0]

    ### filename property
    @property
    def filename(self):
        return self._dbFilename

    @filename.setter
    def filename(self, fn):
            self._dbFilename = fn
            self._db = sqlite3.connect(fn)
            self._db.row_factory = sqlite3.Row

    @filename.deleter
    def filename(self):
        self.close()

    def close(self):
            self._db.close()
            del self._dbFilename

def test():
    import os
    fn = ':memory:'     # in-memory database
    t = 'foo'

    recs = [
        dict( string = 'one' ),
        dict( string = 'two' ),
        dict( string = 'three' )
    ]

    ### for file-based database
    # try: os.stat(fn)
    # except: pass
    # else: 
    #     print('Delete', fn)
    #     os.unlink(fn)

    print('version', __version__)

    print('Create database file {} ...'.format(fn), end = '')
    db = bwDB( filename = fn, table = t )
    print('Done.')

    print('Create table ... ', end='')
    db.sql_do(' DROP TABLE IF EXISTS {} '.format(t))
    db.sql_do(' CREATE TABLE {} ( id INTEGER PRIMARY KEY, string TEXT ) '.format(t))
    print('Done.')

    print('Insert into table ... ', end = '')
    for r in recs: db.insert(r)
    print('Done.')

    print('Read from table')
    for r in db.getrecs(): print(dict(r))

    print('Update table')
    db.update(2, dict(string = 'TWO'))
    print( dict( db.getrec(2) ) )

    print('Insert an extra row ... ', end = '')
    newid = db.insert( dict( string = 'extra' ) )
    print('(id is {})'.format(newid))
    print( dict( db.getrec(newid) ) )
    print('Now delete it')    
    db.delete(newid)
    for r in db.getrecs(): print(dict(r))
    db.close()

if __name__ == "__main__": test()


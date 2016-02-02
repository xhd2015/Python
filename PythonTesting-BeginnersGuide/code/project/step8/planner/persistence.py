import sqlite3
from cPickle import loads, dumps

class file:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)

        try:
            self.connection.execute("""
                create table objects (tag, pickle)
            """)
        except sqlite3.OperationalError:
            pass

    def store_object(self, tag, object):
        self.connection.execute('insert into objects values (?, ?)',
                                (tag, sqlite3.Binary(dumps(object))))

    def load_objects(self, tag):
        cursor = self.connection.execute("""
                     select pickle from objects where tag like ?
                 """, (tag,))
        return [loads(str(row[0])) for row in cursor]

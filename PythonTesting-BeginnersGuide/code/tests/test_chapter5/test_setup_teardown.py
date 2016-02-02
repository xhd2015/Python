class employees:
    def __init__(self, connection):
        self.connection = connection

    def add_employee(self, first, last, date_of_employment):
        cursor = self.connection.cursor()
        cursor.execute('''insert into employees
                            (first, last, date_of_employment)
                          values
                            (:first, :last, :date_of_employment)''',
                       locals())
        self.connection.commit()

        return cursor.lastrowid

    def find_employees_by_name(self, first, last):
        cursor = self.connection.cursor()
        cursor.execute('''select * from employees
                          where
                            first like :first
                          and
                            last like :last''',
                       locals())

        for row in cursor:
            yield row

    def find_employees_by_date(self, date):
        cursor = self.connection.cursor()
        cursor.execute('''select * from employees
                          where date_of_employment = :date''',
                       locals())

        for row in cursor:
            yield row


from unittest import TestCase, main
from sqlite3 import connect, PARSE_DECLTYPES
from datetime import date

class test_employees(TestCase):
    def setUp(self):
        connection = connect(':memory:',
                             detect_types = PARSE_DECLTYPES)
        cursor = connection.cursor()

        cursor.execute('''create table employees
                            (first text,
                             last text,
                             date_of_employment date)''')

        cursor.execute('''insert into employees
                            (first, last, date_of_employment)
                          values
                            ("Test1", "Employee", :date)''',
                       {'date': date(year = 2003,
                                     month = 7,
                                     day = 12)})

        cursor.execute('''insert into employees
                            (first, last, date_of_employment)
                          values
                            ("Test2", "Employee", :date)''',
                       {'date': date(year = 2001,
                                     month = 3,
                                     day = 18)})

        self.connection = connection

    def tearDown(self):
        self.connection.close()

    def test_add_employee(self):
        to_test = employees(self.connection)
        to_test.add_employee('Test1', 'Employee', date.today())

        cursor = self.connection.cursor()
        cursor.execute('''select * from employees
                          order by date_of_employment''')

        self.assertEqual(tuple(cursor),
                         (('Test2', 'Employee', date(year = 2001,
                                                     month = 3,
                                                     day = 18)),
                          ('Test1', 'Employee', date(year = 2003,
                                                     month = 7,
                                                     day = 12)),
                          ('Test1', 'Employee', date.today())))

    def test_find_employees_by_name(self):
        to_test = employees(self.connection)

        found = tuple(to_test.find_employees_by_name('Test1', 'Employee'))
        expected = (('Test1', 'Employee', date(year = 2003,
                                               month = 7,
                                               day = 12)),)

        self.assertEqual(found, expected)

    def test_find_employee_by_date(self):
        to_test = employees(self.connection)

        target = date(year = 2001, month = 3, day = 18)
        found = tuple(to_test.find_employees_by_date(target))

        expected = (('Test2', 'Employee', target),)

        self.assertEqual(found, expected)

if __name__ == '__main__':
    main()

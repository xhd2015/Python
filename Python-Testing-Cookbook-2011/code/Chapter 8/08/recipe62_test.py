import logging
from network import *
import unittest
from springpython.database.factory import *
from springpython.database.core import *

class AbstractEventCorrelatorTests(unittest.TestCase):
    def tearDown(self):
        self.correlator = None

    def test_service_failing(self):
        # This alarm maps to a service.
        evt1 = Event("pyhost1", "serverRestart", 5)

        stored_event, is_active, \
           updated_services, updated_equipment = \
                     self.correlator.process(evt1)

        self.assertEquals(len(updated_services), 1)
        self.assertEquals("service-abc",
               updated_services[0]["service"]["NAME"])
        self.assertEquals("Outage", 
               updated_services[0]["service"]["STATUS"])

        evt2 = Event("pyhost1", "serverRestart", 1)

        stored_event, is_active, \
            updated_services, updated_equipment = \
                 self.correlator.process(evt2)

        self.assertEquals(len(updated_services), 1)
        self.assertEquals("service-abc", 
               updated_services[0]["service"]["NAME"])
        self.assertEquals("Operational", 
               updated_services[0]["service"]["STATUS"])

class MySQLEventCorrelatorTests(AbstractEventCorrelatorTests):
    def setUp(self):
        factory = MySQLConnectionFactory("user", "password", 
                                     "localhost", "recipe62")
        self.correlator = EventCorrelator(factory)

        dt = DatabaseTemplate(factory)
        sql = open("recipe62_network.mysql").read().split(";")
        for statement in sql:
            dt.execute(statement + ";")

class Sqlite3EventCorrelatorTests(AbstractEventCorrelatorTests):
    def setUp(self):
        factory = Sqlite3ConnectionFactory("recipe62.db")
        self.correlator = EventCorrelator(factory)

        dt = DatabaseTemplate(factory)
        sql = open("recipe62_network.sql").read().split(";")
        for statement in sql:
            dt.execute(statement + ";")


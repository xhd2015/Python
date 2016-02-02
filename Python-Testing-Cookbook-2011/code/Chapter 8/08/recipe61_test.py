import logging
from network import *
import unittest
from springpython.database.factory import *
from springpython.database.core import *

class EventCorrelatorEquipmentThreadTests(unittest.TestCase):
    def setUp(self):
        db_name = "recipe61.db"
        factory = Sqlite3ConnectionFactory(db=db_name)
        self.correlator = EventCorrelator(factory)

        dt = DatabaseTemplate(factory)
        sql = open("recipe61_network.sql").read().split(";")
        for statement in sql:
            dt.execute(statement + ";")

    def tearDown(self):
        self.correlator = None

    def test_equipment_failing(self):
        # This alarm maps to a device
        # but doesn't map to any service.

        evt1 = Event("pyhost3", "serverRestart", 5)

        stored_event, is_active, \
           updated_services, updated_equipment = \
                     self.correlator.process(evt1)

        self.assertTrue(is_active)

        self.assertEquals(len(updated_services), 0)
        self.assertEquals(len(updated_equipment), 1)
        self.assertEquals(updated_equipment[0]["HOST_NAME"], 
                                                  "pyhost3")
        # 5 is the value for a failed piece of equipment
        self.assertEquals(updated_equipment[0]["STATUS"], 5)

        evt2 = Event("pyhost3", "serverRestart", 1)

        stored_event, is_active, \
            updated_services, updated_equipment = \
                 self.correlator.process(evt2)

        self.assertFalse(is_active)

        self.assertEquals(len(updated_services), 0)
        self.assertEquals(len(updated_equipment), 1)
        self.assertEquals(updated_equipment[0]["HOST_NAME"], 
                                                  "pyhost3")
        # 1 is the value for a clear piece of equipment
        self.assertEquals(updated_equipment[0]["STATUS"], 1)

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

import logging
from network import *
import unittest
from springpython.database.factory import *
from springpython.database.core import *

class EventCorrelatorUnitTests(unittest.TestCase):
    def setUp(self):
        db_name = "recipe59.db"
        factory = Sqlite3ConnectionFactory(db=db_name)
        self.correlator = EventCorrelator(factory)

        # We "unplug" the DatabaseTemplate so that 
        # we don't talk to a real database.
        self.correlator.dt = None

        # Instead, we create a dictionary of 
        # canned data to return back
        self.return_values = {}

        # For each sub-function of the network app,
        # we replace them with stubs which return our
        # canned data.

        def stub_store_event(event):
            event.id = self.return_values["id"]
            return event, self.return_values["active"]
        self.correlator.store_event = stub_store_event

        def stub_impact(event):
            return (self.return_values["services"], 
                    self.return_values["equipment"])
        self.correlator.impact = stub_impact

        def stub_update_service(service, event):
            return service + " updated"
        self.correlator.update_service = stub_update_service

        def stub_update_equip(equip, event):
            return equip + " updated"
        self.correlator.update_equipment = stub_update_equip

    def test_process_events(self):
        # For this test case, we can preload the canned data,
        # and verify that our process function is working
        # as expected without touching the database.

        self.return_values["id"] = 4668
        self.return_values["active"] = True
        self.return_values["services"] = ["service1", 
                                          "service2"]
        self.return_values["equipment"] = ["device1"]

        evt1 = Event("pyhost1", "serverRestart", 5)

        stored_event, is_active, \
           updated_services, updated_equipment = \
                     self.correlator.process(evt1)

        self.assertEquals(4668, stored_event.id)
        self.assertTrue(is_active)
 
        self.assertEquals(2, len(updated_services))
        self.assertEquals(1, len(updated_equipment))

class EventCorrelatorIntegrationTests(unittest.TestCase):
    def setUp(self):
        db_name = "recipe59.db"
        factory = Sqlite3ConnectionFactory(db=db_name)
        self.correlator = EventCorrelator(factory)
        dt = DatabaseTemplate(factory)
        sql = open("network.sql").read().split(";")
        for statement in sql:
            dt.execute(statement + ";")

    def test_process_events(self):
        evt1 = Event("pyhost1", "serverRestart", 5)

        stored_event, is_active, \
           updated_services, updated_equipment = \
                     self.correlator.process(evt1)

        print "Stored event: %s" % stored_event
        if is_active:
            print "This event was an active event."

        print "Updated services: %s" % updated_services
        print "Updated equipment: %s" % updated_equipment
        print "---------------------------------"


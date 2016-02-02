import unittest
from network import *
from springpython.database.factory import *

class ManagementDemo(unittest.TestCase):
    def setUp(self):
        factory = MySQLConnectionFactory("user", "password", 
                                     "localhost", "recipe62")
        self.correlator = EventCorrelator(factory)

        dt = DatabaseTemplate(factory)
        sql = open("recipe62_network.mysql").read().split(";")
        for statement in sql:
            dt.execute(statement + ";")

    def test_processing_a_service_affecting_event(self):
        # Define a service-affecting event
        evt1 = Event("pyhost1", "serverRestart", 5)

        # Inject it into the system
        stored_event, is_active, \
           updated_services, updated_equipment = \
                     self.correlator.process(evt1)

        # These are the values I plan to call
        # attention to during my demo
        self.assertEquals(len(updated_services), 1)
        self.assertEquals("service-abc",
               updated_services[0]["service"]["NAME"])
        self.assertEquals("Outage", 
               updated_services[0]["service"]["STATUS"])


if __name__ == "__main__":
    unittest.main()

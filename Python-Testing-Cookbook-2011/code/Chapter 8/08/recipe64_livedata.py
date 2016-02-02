import random
import sys
import time
from network import *
from springpython.remoting.pyro import *

print "Sending events to live network app. Ctrl+C to exit..."
proxy = PyroProxyFactory()
proxy.service_url = "PYROLOC://127.0.0.1:7766/network_advised"

while True:
    hostname = random.choice(["pyhost1","pyhost2","pyhost3"])
    condition = random.choice(["serverRestart", "lineStatus"])
    severity = random.choice([1,5])

    evt = Event(hostname, condition, severity)

    stored_event, is_active, updated_services, \
         updated_equipment = proxy.process(evt)
    print "Stored event: %s" % stored_event
    print "Active? %s" % is_active
    print "Services updated: %s" % updated_services
    print "Equipment updated; %s" % updated_equipment
    print "================"

    time.sleep(random.choice(range(1,10)))


from springpython.remoting.pyro import *
from datetime import datetime
import pickle
import time

with open("recipe65_data.txt") as f:
    lines = f.readlines()
events = [pickle.loads(line.replace("&&&", "\n")) 
                                      for line in lines]

print "Sending events to live network app. Ctrl+C to exit..."
proxy = PyroProxyFactory()
proxy.service_url = "PYROLOC://127.0.0.1:7766/network"

for (e, time_it_happened) in events:
    stored_event, is_active, updated_services, \
         updated_equipment = proxy.process(e)

    print "Stored event: %s" % stored_event
    print "Active? %s" % is_active
    print "Services updated: %s" % updated_services
    print "Equipment updated; %s" % updated_equipment
    print "================"

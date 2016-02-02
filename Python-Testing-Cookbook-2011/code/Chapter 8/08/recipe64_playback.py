from springpython.remoting.pyro import *
from datetime import datetime
import pickle
import time

with open("recipe64_data.txt") as f:
    lines = f.readlines()
events = [pickle.loads(line.replace("&&&", "\n")) 
                                      for line in lines]

def calc_offset(evt, time_it_happened, previous_time):
    if previous_time is None:
        return time_it_happened - time_it_happened
    else:
        return time_it_happened - previous_time

print "Sending events to live network app. Ctrl+C to exit..."
proxy = PyroProxyFactory()
proxy.service_url = "PYROLOC://127.0.0.1:7766/network"

previous_time = None
for (e, time_it_happened) in events:
    diff = calc_offset(e, time_it_happened, previous_time)

    print "Original: %s Now: %s" % (time_it_happened, datetime.now())

    stored_event, is_active, updated_services, \
         updated_equipment = proxy.process(e)

    print "Stored event: %s" % stored_event
    print "Active? %s" % is_active
    print "Services updated: %s" % updated_services
    print "Equipment updated; %s" % updated_equipment
    print "Next event in %s seconds" % diff.seconds
    print "================"

    time.sleep(diff.seconds) 

    previous_time = time_it_happened

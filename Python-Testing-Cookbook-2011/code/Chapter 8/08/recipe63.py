import getopt
import random
import sys
import time
from network import *
from springpython.remoting.pyro import *

def usage():
    print "Usage"
    print "====="
    print "-h, --help           read this help"
    print "-r, --rate [arg]     number of events per second"
    print "-d, --demo           demo by printing events"

try:
    opts, args = getopt.getopt(sys.argv[1:], "hr:d", ["help", "rate=", "demo"])
except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(1)
        
rate = 10
demo_mode = False

for o, a in opts:
    if o in ("-h", "--help"):
        usage()
        sys.exit(1)
    elif o in ("-r", "--rate"):
        rate = a
    elif o in ("-d", "--demo"):
        demo_mode = True

if not demo_mode:
    print "Sending events to live network app. Ctrl+C to exit..."
    proxy = PyroProxyFactory()
    proxy.service_url = "PYROLOC://127.0.0.1:7766/network"

while True:
    hostname = random.choice(["pyhost1","pyhost2","pyhost3"])
    condition = random.choice(["serverRestart", "lineStatus"])
    severity = random.choice([1,5])

    evt = Event(hostname, condition, severity)

    if demo_mode:
        now = time.strftime("%a, %d %b %Y %H:%M:%S +0000", 
                                          time.localtime())
        print "%s: Sending out %s" % (now, evt)
    else:
        stored_event, is_active, updated_services, \
             updated_equipment = proxy.process(evt)
        print "Stored event: %s" % stored_event
        print "Active? %s" % is_active
        print "Services updated: %s" % updated_services
        print "Equipment updated; %s" % updated_equipment
        print "================"

    time.sleep(1.0/float(rate))


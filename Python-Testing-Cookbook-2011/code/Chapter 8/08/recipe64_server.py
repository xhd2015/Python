from springpython.database.factory import *
from springpython.database.core import *
from springpython.remoting.pyro import *
from springpython.aop import *

from network import *
from datetime import datetime
import os
import os.path
import pickle

import logging
logger = logging.getLogger("springpython.remoting")
loggingLevel = logging.DEBUG
logger.setLevel(loggingLevel)
ch = logging.StreamHandler()
ch.setLevel(loggingLevel)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

# Initialize the database
factory = MySQLConnectionFactory("user", "password", 
                                 "localhost", "recipe64")
dt = DatabaseTemplate(factory)
sql = open("recipe62_network.mysql").read().split(";")
for statement in sql:
    dt.execute(statement + ";")

# Create an instance of the network management app
target_service = EventCorrelator(factory)

# Expose the original network app as a Pyro service
unadvised_service = PyroServiceExporter()
unadvised_service.service_name = "network"
unadvised_service.service = target_service
unadvised_service.after_properties_set()

class Recorder(MethodInterceptor):
    """
    An interceptor that catches each event,
    write it to disk, then proceeds to the
    network management app.
    """
    def __init__(self):
        self.filename = "recipe64_data.txt"
        self.special_char = "&&&"
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def invoke(self, invocation):
        # Write data to disk
        with open(self.filename, "a") as f:
            evt = invocation.args[0]
            now = datetime.now()
            output = (evt, now)
            print "Recording %s" % evt
            f.write(pickle.dumps(output).replace(
                               "\n", "&&&") + "\n")
     
        # Now call the advised service
        return invocation.proceed()

# Wrap the network app with an interceptor
advisor = ProxyFactoryObject()
advisor.target = target_service
advisor.interceptors = [Recorder()]

# Expose the advised network app as a Pyro service
advised_service = PyroServiceExporter()
advised_service.service_name = "network_advised"
advised_service.service = advisor
advised_service.after_properties_set()


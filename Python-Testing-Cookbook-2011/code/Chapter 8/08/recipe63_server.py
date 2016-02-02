from springpython.database.factory import *
from springpython.database.core import *
from springpython.remoting.pyro import *

from network import *

import logging
logger = logging.getLogger("springpython")
loggingLevel = logging.DEBUG
logger.setLevel(loggingLevel)
ch = logging.StreamHandler()
ch.setLevel(loggingLevel)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

# Initialize the database
factory = MySQLConnectionFactory("user", "password", 
                                 "localhost", "recipe63")
dt = DatabaseTemplate(factory)
sql = open("recipe62_network.mysql").read().split(";")
for statement in sql:
    dt.execute(statement + ";")

# Create an instance of the network management app
target_service = EventCorrelator(factory)

# Expose the network app as a Pyro service
exporter = PyroServiceExporter()
exporter.service_name = "network"
exporter.service = target_service
exporter.after_properties_set()



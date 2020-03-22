import logging
__version__="0.1"
log_level_str = "debug"
log_level = logging.INFO
if log_level_str == "debug":
    log_level = logging.DEBUG

address_mongo = "192.168.1.5"
port_mongo = 27017
log_file = "test.log"
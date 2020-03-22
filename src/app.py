import argparse
import logging

from src import log_file, log_level, address_mongo, port_mongo
from flask import Flask
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient

from src.modules.test import Test
from src.modules.user import User
from src.utils import setup_logger
MAIN_LOGGER = setup_logger(logging.getLogger("MAIN"), log_level, log_file)

def parse_argument():
    parser = argparse.ArgumentParser(description="Test program", usage="python3 -m src [option]")
    parser.add_argument("--address", "-a", default="0.0.0.0", help="Host")
    parser.add_argument("--port", "-p", default=8080, help="Port")
    args = parser.parse_args()
    return args
def main(args):
    MAIN_LOGGER.info("Hello world, info")
    MAIN_LOGGER.debug("Arguments: host: {}, port: {}".format(args.address, args.port))
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Test, "/api/test/v1.0/test")
    api.add_resource(User, "/api/test/v1.0/user")
    app.run(debug=log_level==logging.DEBUG, host=args.address, port=args.port)




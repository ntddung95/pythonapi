import logging
from pymongo import MongoClient
from flask_restful import Resource, reqparse
from src import log_file, log_level, address_mongo, port_mongo
from src.utils import setup_logger
USER_LOGGER = setup_logger(logging.getLogger("USER"), log_level, log_file)

class User(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str)
        parser.add_argument("password", type=str)
        body_args = parser.parse_args()
        USER_LOGGER.debug("Username: {}".format(body_args.username))
        mongodb_client = MongoClient(address_mongo, port_mongo)
        db = mongodb_client.ecg
        collection = db.user
        res = collection.find_one({"username":body_args.username})
        if res is None:
            return {"message":"User not existed"}, 500
        if body_args.password == res["password"]:
            return {"message":"OK"}, 200
        else:
            return {"message":"Wrong password"}, 401
        USER_LOGGER.debug("Result: {}".format(res))
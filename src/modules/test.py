import logging
from flask_restful import Resource
from src import log_file, log_level
from src.utils import setup_logger
TEST_LOGGER = setup_logger(logging.getLogger("TEST"), log_level, log_file)
class Test(Resource):
    def get(self):
        TEST_LOGGER.debug("Get test API")
        return {"message":"Test get API"},401
    def post(self):
        TEST_LOGGER.debug("Post test API")
        pass
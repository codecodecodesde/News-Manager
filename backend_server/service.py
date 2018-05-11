"""Backend Service"""
import operations
import logging

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

LOGGER_FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
LOGGER = logging.getLogger('backend_service')
LOGGER.setLevel(logging.DEBUG)

#dummy function for testing rpc server
def add(num1, num2):
    print("add is called with %d and %d" % (num1, num2))
    return num1 + num2

def getOneNews():
    """ Test method to get one news """
    LOGGER.debug("getOneNews is called")
    return operations.getOneNews()

def getNewsSummariesForUser(user_id, page_num):
    """ Get news summaries for a user """
    LOGGER.debug("get_news_summaries_for_user is called with %s and %s", user_id, page_num)
    return operations.getNewsSummariesForUser(user_id, page_num)

def log_news_click_for_user(user_id, news_id):
    """ Log a news click event for a user. """
    LOGGER.debug("log_news_click_for_user is called with %s and %s", user_id, news_id)
    operations.logNewsClickForUser(user_id, news_id)

RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(getOneNews, 'getOneNews')
RPC_SERVER.register_function(getNewsSummariesForUser, 'getNewsSummariesForUser')
RPC_SERVER.register_function(log_news_click_for_user, 'logNewsClickForUser')

LOGGER.info("Starting RPC server on %s:%d", SERVER_HOST, SERVER_PORT)

RPC_SERVER.serve_forever()

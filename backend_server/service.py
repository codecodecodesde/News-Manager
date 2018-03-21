"""Backend Service"""
import operations

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

#dummy function for testing rpc server
def add(num1, num2):
    print("add is called with %d and %d" % (num1, num2))
    return num1 + num2

def getOneNews():
    print("getOneNews is called")
    return operations.getOneNews()

RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(getOneNews, 'getOneNews')
RPC_SERVER.serve_forever()

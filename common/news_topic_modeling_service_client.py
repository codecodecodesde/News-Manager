import jsonrpclib

URL = "http://localhost:6060"

client = jsonrpclib.ServerProxy(URL)

def classify(text):
    topic = client.classify(text)
    return topic

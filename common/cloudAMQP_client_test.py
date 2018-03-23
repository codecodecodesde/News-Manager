from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://iyivlewx:Cd0kAm5crqwb8lcNZ_XVvbUMDPmI_7it@skunk.rmq.cloudamqp.com/iyivlewx"
QUEUE_NAME = "demo"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, QUEUE_NAME)

    sentMsg = {"tesst": "test"}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg

    print('test_basic passed')

if __name__ == "__main__":
    test_basic()

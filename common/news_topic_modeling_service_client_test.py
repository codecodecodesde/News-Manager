import news_topic_modeling_service_client as client

def test_basic():
    newsTitle = "Pentagon might propose ground troops for Syria"
    topic = client.classify(newsTitle)
    #assert topic == "U.S."
    print(topic)

if __name__ == "__main__":
    test_basic()

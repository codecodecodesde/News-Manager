import os
import sys

#from newspaper import Article

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))
import cnn_news_scraper

from cloudAMQP_client import CloudAMQPClient

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://gxoshjxp:jUcy9JVFqWn5Zm-ryAcARjucv6wTUvyZ@skunk.rmq.cloudamqp.com/gxoshjxp"
DEDUPE_NEWS_TASK_QUEUE_NAME = "news-manager-dedupe-task"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://iyivlewx:Cd0kAm5crqwb8lcNZ_XVvbUMDPmI_7it@skunk.rmq.cloudamqp.com/iyivlewx"
SCRAPE_NEWS_TASK_QUEUE_NAME = "news-manager-scrape-task"

SLEEP_TIME_IN_SECONDS = 5

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print("message is broken")
        return

    task = msg
    text = None

    #support CNN only
    if task['source'] == 'cnn':
        print('scraping CNN news')
        text = cnn_news_scraper.extract_news(task['url'])
    else:
        return

    task['text'] = text
    dedupe_news_queue_client.sendMessage(task)


def run():
    while True:
        if scrape_news_queue_client is not None:
            msg = scrape_news_queue_client.getMessage()
            if msg is not None:
                try:
                    handle_message(msg)
                except Exception as e:
                    print(e)
                    pass

            scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)

if __name__ == "__main__":
    run()

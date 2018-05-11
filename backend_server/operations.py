import json
import os
import pickle
import redis
import sys

from bson.json_util import dumps
from datetime import datetime

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import news_recommendation_service_client

from cloudAMQP_client import CloudAMQPClient


REDIS_HOST = "localhost"
REDIS_PORT = 6379

NEWS_LIMIT = 500
NEWS_LIST_BATCH_SIZE = 10
USER_NEWS_TIME_OUT_IN_SECONDS = 60 * 60

NEWS_TABLE_NAME = "news"

LOG_CLICKS_TASK_QUEUE_URL = "amqp://wgdfwyqw:Iv5HoJx5d-BXCnE0ApfJDURfGxMcirZU@wasp.rmq.cloudamqp.com/wgdfwyqw"
LOG_CLICKS_TASK_QUEUE_NAME = "news-manager-clicklog-queue"

redis_client = redis.StrictRedis()

cloudAMQP_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)

def getOneNews():
    db = mongodb_client.get_db()
    news = db[NEWS_TABLE_NAME].find_one()
    return json.loads(dumps(news))


def getNewsSummariesForUser(user_id, page_num):
    page_num = int(page_num)

    if page_num <= 0:
        return []

    begin_index = (page_num - 1) * NEWS_LIST_BATCH_SIZE
    end_index = page_num * NEWS_LIST_BATCH_SIZE

    # The final list of news to be returned.
    sliced_news = []
    db = mongodb_client.get_db()

    if redis_client.get(user_id) is not None:
        news_digests = pickle.loads(redis_client.get(user_id))

        sliced_news_digests = news_digests[begin_index:end_index]
        sliced_news = list(db[NEWS_TABLE_NAME].find({'digest':{'$in':sliced_news_digests}}))
    else:
        total_news = list(db[NEWS_TABLE_NAME].find().sort([('publishedAt', -1)]).limit(NEWS_LIMIT))

        total_news_digests = [x['digest'] for x in total_news]

        redis_client.set(user_id, pickle.dumps(total_news_digests))
        redis_client.expire(user_id, USER_NEWS_TIME_OUT_IN_SECONDS)

        sliced_news = total_news[begin_index:end_index]


    # Get preference for the user
    # TODO: use preference to customize returned news list.
    preference = news_recommendation_service_client.getPreferenceForUser(user_id)
    topPreference = None

    if preference is not None and len(preference) > 0:
        topPreference = preference[0]
    
    for news in sliced_news:
        # Remove text field to save bandwidth.
        del news['text']
        if 'class' in news and news['class'] == topPreference:
            news['reason'] = 'Recommend'

    return json.loads(dumps(sliced_news))


def logNewsClickForUser(user_id, news_id):
    message = {'userId':user_id, 'newsId':news_id, 'timestamp':str(datetime.utcnow())}
    
    # Send log message to click log processor.
    cloudAMQP_client.sendMessage(message);

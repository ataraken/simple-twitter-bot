import datetime
import logging

import azure.functions as func

from shared_code.twitter import get_oldest_timeline_tweet
from shared_code.twitter.api.v1 import twitter_proxy
from shared_code.twitter.api.v1 import twitter_destroy_helper
from shared_code.twitter.api.v1 import twitter_update_helper

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    try:
        logging.info(f'Python timer trigger function. Getting oldest tweet at %s', utc_timestamp)
        id, text = get_oldest_timeline_tweet.get()

        logging.info(f'Python timer trigger function. Upload tweet at %s', utc_timestamp)
        param = twitter_update_helper.Param(text)
        twitter_proxy.request(param, param.get_session())

        logging.info(f'Python timer trigger function. Deleting oldest tweet at %s', utc_timestamp)
        param = twitter_destroy_helper.Param(id)
        twitter_proxy.request(param, param.get_session())
    except Exception as e:
        logging.error(f'Python timer trigger function. %s %s', e, utc_timestamp)
    
    logging.info('Python timer trigger function exit at %s', utc_timestamp)

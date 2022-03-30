import datetime
import logging

import azure.functions as func

from shared_code import twitter_friends_ids_helper
from shared_code import twitter_followers_ids_hepler
from shared_code import twitter_friendships_destroy_helper

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    try:
        param = twitter_friends_ids_helper.Param()
        friends = twitter_friends_ids_helper.request(param)

        param = twitter_followers_ids_hepler.Param()
        followers = twitter_followers_ids_hepler.request(param)

        targets = [ id for id in friends['ids'] if not id in followers['ids'] ]

        for id in targets:
            param = twitter_friendships_destroy_helper.Param(id)
            twitter_friendships_destroy_helper.request(param)

    except Exception as e:
        logging.info(f'Python timer trigger function. %s %s', e, utc_timestamp)

    logging.info('Python timer trigger function exit at %s', utc_timestamp)
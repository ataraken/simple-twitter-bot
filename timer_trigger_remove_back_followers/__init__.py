import datetime
import logging

import azure.functions as func

from shared_code.twitter.api.v1 import proxy
from shared_code.twitter.api.v1 import friends_ids
from shared_code.twitter.api.v1 import followers_ids
from shared_code.twitter.api.v1 import friendships_destroy

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    try:
        param = friends_ids.Param()
        friends = proxy.request(param, param.get_session())

        param = followers_ids.Param()
        followers = proxy.request(param, param.get_session())

        targets = [ id for id in friends['ids'] if not id in followers['ids'] ]

        for id in targets:
            param = friendships_destroy.Param(id)
            proxy.request(param, param.get_session())

    except Exception as e:
        logging.error(f'Python timer trigger function. %s %s', e, utc_timestamp)

    logging.info('Python timer trigger function exit at %s', utc_timestamp)
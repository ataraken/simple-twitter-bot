"""timer trigger tweet function

タイマートリガーによって呼び出され、
対象アカウントのタイムラインのもっとも古いツィートの文言をツィートする。
最も古いツィートは削除する。
"""
import datetime
import logging

import azure.functions as func

from shared_code.twitter import get_oldest_timeline_tweet
from shared_code.twitter.api.v1 import proxy
from shared_code.twitter.api.v1 import destroy
from shared_code.twitter.api.v1 import update

def main(mytimer: func.TimerRequest) -> None:
    """main関数

    Args:
        mytimer
    """    
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    try:
        logging.info(f'Python timer trigger function. Getting oldest tweet at %s', utc_timestamp)
        id, text = get_oldest_timeline_tweet.get()

        logging.info(f'Python timer trigger function. Upload tweet at %s', utc_timestamp)
        param = update.Param(text)
        proxy.request(param, param.get_session())

        logging.info(f'Python timer trigger function. Deleting oldest tweet at %s', utc_timestamp)
        param = destroy.Param(id)
        proxy.request(param, param.get_session())
    except Exception as e:
        logging.error(f'Python timer trigger function. %s %s', e, utc_timestamp)
    
    logging.info('Python timer trigger function exit at %s', utc_timestamp)

import datetime
import logging

import azure.functions as func

from shared_code import get_oldest_timeline_tweet
from shared_code import twitter_update_helper

def main(mytimer: func.TimerRequest) -> None:

  utc_timestamp = datetime.datetime.utcnow().replace(
    tzinfo=datetime.timezone.utc).isoformat()

  if mytimer.past_due:
    logging.info('The timer is past due!')

  logging.info('Python timer trigger function ran at %s', utc_timestamp)

  id, text = get_oldest_timeline_tweet.get()

  param = twitter_update_helper.Param(text)
  twitter_update_helper.request(param)

  logging.info('Python timer trigger function exit at %s', utc_timestamp)

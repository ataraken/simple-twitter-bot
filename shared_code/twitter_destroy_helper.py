# <project_root>/shared_code/twitter_destroy_helper.py

import json
from shared_code import twitter_oauth_helper

class Param:
  def __init__(self, id: int):
    self._tweet_id = id
    self._param = {
      'trim_user': None
    }

  def convert_to_query(self) -> str:
    return { k: self._param[k] for k in self._param if None != self._param[k] }

  def get_tweet_id(self) -> int:
    return self._tweet_id

def request(param):
  endpoint_url = f'https://api.twitter.com/1.1/statuses/destroy/{param.get_tweet_id()}.json'

  client = twitter_oauth_helper.create_session()

  params = param.convert_to_query()

  if len(params) == 0:
    res = client.post(endpoint_url)
  else:
    res = client.post(endpoint_url, params=params)

  if res.status_code == 200:
    res = json.loads(res.text)
  else:
    raise RuntimeError('Network Error. status code: {res.status_code}')

  return res

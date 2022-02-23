# <project_root>/shared_code/twitter_timeline_helper.py

from os import environ
from shared_code import twitter_oauth_helper
import twitter_oauth_helper

class Param:
  def __init__(self):
    self._param = {
      'user_id': environ['TWITTER_USER_ID'],
      'tweet_mode': 'extended',
      'count': None,
      'since_id': None,
      'max_id': None,
      'trim_user': None,
      'exclude_replies': None,
      'include_entities': None,
    }

  def convert_to_query(self) -> str:
    return { k: self._param[k] for k in self._param if None != self._param[k] }

  def set_user_id(self, id: str) -> None:
    self._param['user_id'] = id

  def set_count(self, cnt: int) -> None:
    if cnt <= 200:
      self._param['count'] = cnt
    elif cnt <= 0:
      self._param['count'] = 1
    else:
      self._param['count'] = 200

  def set_max_id(self, id: int) -> None:
    self._param['max_id'] = id

  def get_user_id(self) -> str:
    return self._param['user_id']

  def get_count(self) -> int:
    return self._param['count']

  def get_since_id(self) -> str:
    return self._param['since_id']

  def get_max_id(self) -> int:
    return self._param['max_id']

  def get_trim_user(self) -> str:
    return self._param['trim_user']

  def get_exclude_replies(self) -> str:
    return self._param['exclude_replies']

  def get_include_entitles(self) -> str:
    return self._param['include_entitles']

  def get_tweet_mode(self) -> str:
    return self._param['tweet_mode']

def request(param):
  endpoint_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

  client = twitter_oauth_helper.create_session()

  params = param.convert_to_query()

  if len(params) == 0:
    res = client.get(endpoint_url)
  else:
    res = client.get(endpoint_url, params=params)

  if res.status_code == 200:
    res = json.loads(res.text)
  else:
    raise RuntimeError('Network Error. status code: {res.status_code}')

  return res

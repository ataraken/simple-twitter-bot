# <project_root>/shared_code/twitter_followers_ids_helper.py

import json
from os import environ
from shared_code import twitter_oauth_helper

class Param:
  def __init__(self):
    self._param = {
      'user_id': environ['TWITTER_USER_ID'],
      'screen_name': None,
      'cursor': None,
      'stringify_ids': None,
      'count': 5000
    }

  def convert_to_query(self) -> str:
    return { k: self._param[k] for k in self._param if None != self._param[k] }

  def set_user_id(self, id: str) -> None:
    self._param['user_id'] = id

  def set_screen_name(self, name: str) -> None:
    self._param['screen_name'] = name

  def set_cursor(self, cursor: str) -> None:
    self._param['cursor'] = cursor

  def set_stringify_ids(self, stringify_ids: str) -> None:
    self._param['stringify_ids'] = stringify_ids

  def set_count(self, cnt: int) -> None:
    up_to_count = 5000

    if cnt <= up_to_count:
      self._param['count'] = cnt
    elif cnt <= 0:
      self._param['count'] = 1
    else:
      self._param['count'] = up_to_count

def request(param: Param) -> str:
  endpoint_url = 'https://api.twitter.com/1.1/followers/ids.json'

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

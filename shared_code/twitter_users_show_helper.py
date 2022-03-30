# <project_root>/shared_code/twitter_friends_users_show_helper.py

import json
from shared_code import twitter_oauth_helper

class Param:
  def __init__(self):
    self._param = {
      'user_id': None,
      'include_entities': None,
      'include_entities': None
    }

  def convert_to_query(self) -> str:
    return { k: self._param[k] for k in self._param if None != self._param[k] }

  def set_user_id(self, id: str) -> None:
    self._param['user_id'] = id

  def set_screen_name(self, name: str) -> None:
    self._param['screen_name'] = name

  def set_include_entities(self, flag: bool) -> None:
    self._param['cursor'] = flag

def request(param: Param) -> str:
  endpoint_url = 'https://api.twitter.com/1.1/users/show.json'

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

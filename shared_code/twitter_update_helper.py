# <project_root>/shared_code/twitter_update_helper.py

import json
from shared_code import twitter_oauth_helper

class Param:
  def __init__(self, status: str):
    self._param = {
      'status': status
    }

  def convert_to_query(self) -> str:
    return { k: self._param[k] for k in self._param if None != self._param[k] }

def request(param: Param) -> str:
  endpoint_url = 'https://api.twitter.com/1.1/statuses/update.json'

  client = twitter_oauth_helper.create_session()

  params = param.convert_to_query()

  res = client.post(endpoint_url, params=params)

  if res.status_code == 200:
    res = json.loads(res.text)
  else:
    raise RuntimeError('Network Error. status code: {res.status_code}')

  return res
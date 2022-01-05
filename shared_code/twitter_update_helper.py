# <project_root>/shared_code/twitter_update_helper.py

import json
from shared_code import twitter_oauth_helper

class Param:
  def __init__(self, status):
    self._status= status

  def get_status(self):
    return self._status

def request(param):
  endpoint_url = 'https://api.twitter.com/1.1/statuses/update.json'

  client = twitter_oauth_helper.create_session()

  params = {}
  params['status'] = param.get_status()

  res = client.post(endpoint_url, params=params)

  if res.status_code == 200:
    res = json.loads(res.text)
  else:
    res = json.loads(res.text)

  return res
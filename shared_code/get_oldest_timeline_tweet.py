# <project_root>/shared_code/get_oldest_timeline_tweet.py

from shared_code import twitter_proxy
from shared_code import twitter_timeline_helper

def get():
    cnt = 200
    is_exit = False
    max_id = None

    while not is_exit:
        param = twitter_timeline_helper.Param()
        param.set_count(cnt)
        param.set_max_id(max_id)

        timeline = twitter_proxy.request(param, param.get_session())
        is_exit = len(timeline) != cnt

        record = timeline[-1]
        max_id = record['id']
  
    return record['id'], record['full_text']

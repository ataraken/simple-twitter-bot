# <project_root>/shared_code/twitter_destroy_helper.py

from shared_code.twitter.api.v1 import proxy

class Param(proxy.ParamInterface):
    def __init__(self, id: int):
        super().__init__()
        self._tweet_id = id
        self._param = {
            'trim_user': None
        }

    def get_tweet_id(self) -> int:
        return self._tweet_id

    def get_endpoint_url(self) -> str:
        return f'https://api.twitter.com/1.1/statuses/destroy/{self.get_tweet_id()}.json'

    def get_session(self) -> object:
        return self._session.post


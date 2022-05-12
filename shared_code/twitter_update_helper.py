# <project_root>/shared_code/twitter_update_helper.py

from shared_code import twitter_proxy

class Param(twitter_proxy.ParamInterface):
    def __init__(self, status: str):
        super().__init__()
        self._param = {
            'status': status
        }

    def get_endpoint_url(self) -> str:
        return 'https://api.twitter.com/1.1/statuses/update.json'

    def get_session(self) -> object:
        return self._session.post

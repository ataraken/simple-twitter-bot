# <project_root>/shared_code/update.py

from shared_code.twitter.api.v1 import proxy

class Param(proxy.ParamInterface):
    def __init__(self, status: str):
        super().__init__()
        self._param = {
            'status': status
        }

    def get_endpoint_url(self) -> str:
        return 'https://api.twitter.com/1.1/statuses/update.json'

    def get_session(self) -> object:
        return self._session.post

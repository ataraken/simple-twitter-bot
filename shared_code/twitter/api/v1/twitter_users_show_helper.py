# <project_root>/shared_code/twitter_friends_users_show_helper.py

from shared_code.twitter.api.v1 import twitter_proxy

class Param(twitter_proxy.ParamInterface):
    def __init__(self):
        super().__init__()
        self._param = {
            'user_id': None,
            'include_entities': None,
            'include_entities': None
        }

    def set_user_id(self, id: str) -> None:
        self._param['user_id'] = id

    def set_screen_name(self, name: str) -> None:
        self._param['screen_name'] = name

    def set_include_entities(self, flag: bool) -> None:
        self._param['cursor'] = flag

    def get_session(self) -> object:
        return self._session.post

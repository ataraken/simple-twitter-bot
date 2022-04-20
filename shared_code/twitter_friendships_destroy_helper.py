# <project_root>/shared_code/twitter_friends_users_show_helper.py

from shared_code import twitter_proxy

class Param(twitter_proxy.ParamInterface):
    def __init__(self, user_id: int):
        self._param = {
            'screen_name': None,
            'user_id': user_id
        }

    def set_user_id(self, id: int) -> None:
        self._param['user_id'] = id

    def set_screen_name(self, name: str) -> None:
        self._param['screen_name'] = name

    def get_user_id(self) -> int:
        return self._param['user_id']

    def get_screen_name(self) -> str:
        return self._param['screen_name']

    def get_endpoint_url(self) -> str:
        return 'https://api.twitter.com/1.1/friendships/destroy.json'

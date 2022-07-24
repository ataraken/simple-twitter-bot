"""GET friends/ids API

follower のリストを取得します。
follower は対象アカウントをフォローしているユーザーのことです。

https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/get-followers-ids
"""

from os import environ
from shared_code.twitter.api.v1 import proxy

class Param(proxy.ParamInterface):
    """GET friends/ids API のパラメーター

    Attributes:
        _param: パラメーター
    """
    def __init__(self):
        """コンストラクタ"""
        super().__init__()
        self._param = {
            'user_id': environ['TWITTER_USER_ID'],
            'screen_name': None,
            'cursor': None,
            'stringify_ids': None,
            'count': 5000
        }

    def set_user_id(self, id: str) -> None:
        self._param['user_id'] = id

    def get_user_id(self) -> None:
        return self._param['user_id']

    def set_screen_name(self, name: str) -> None:
        self._param['screen_name'] = name

    def get_screen_name(self) -> str:
        return self._param['screen_name']

    def set_cursor(self, cursor: str) -> None:
        self._param['cursor'] = cursor

    def get_cursor(self) -> str:
        return self._param['cursor']

    def set_stringify_ids(self, stringify_ids: str) -> None:
        self._param['stringify_ids'] = stringify_ids

    def get_stringify_ids(self) -> str:
        return self._param['stringify_ids']

    def set_count(self, cnt: int) -> None:
        up_to_count = 5000

        if cnt <= 0:
            self._param['count'] = 1
        elif cnt <= up_to_count:
            self._param['count'] = cnt
        else:
            self._param['count'] = up_to_count

    def get_count(self) -> int:
        return self._param['count']

    def get_endpoint_url(self) -> str:
        return 'https://api.twitter.com/1.1/followers/ids.json'

    def get_session(self) -> object:
        return self._session.get

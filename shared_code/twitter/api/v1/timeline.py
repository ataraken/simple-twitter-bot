"""GET statuses/user_timeline API

対象アカウントのタイムラインを取得するための情報を保持します。

https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline
"""

from os import environ
from shared_code.twitter.api.v1 import proxy

class Param(proxy.ParamInterface):
    """GET statuses/user_timeline API のパラメーター"""

    def __init__(self):
        """コンストラクタ

        Attributes:
            _param: パラメーター
        """
        super().__init__()
        self._param = {
            'user_id': environ['TWITTER_USER_ID'],
            'tweet_mode': 'extended',
            'count': None,
            'since_id': None,
            'max_id': None,
            'trim_user': None,
            'exclude_replies': None,
            'include_rts': None,
        }

    def set_user_id(self, id: str) -> None:
        self._param['user_id'] = id

    def get_user_id(self) -> str:
        return self._param['user_id']

    def set_count(self, cnt: int) -> None:
        if cnt <= 0:
            self._param['count'] = 1
        elif cnt <= 200:
            self._param['count'] = cnt
        else:
            self._param['count'] = 200

    def get_count(self) -> int:
        return self._param['count']

    def set_max_id(self, id: int) -> None:
        self._param['max_id'] = id

    def get_since_id(self) -> str:
        return self._param['since_id']

    def get_max_id(self) -> int:
        return self._param['max_id']

    def get_trim_user(self) -> str:
        return self._param['trim_user']

    def get_exclude_replies(self) -> str:
        return self._param['exclude_replies']

    def get_include_entitles(self) -> str:
        return self._param['include_rts']

    def get_tweet_mode(self) -> str:
        return self._param['tweet_mode']

    def get_endpoint_url(self) -> str:
        return 'https://api.twitter.com/1.1/statuses/user_timeline.json'

    def get_session(self) -> object:
        return self._session.get

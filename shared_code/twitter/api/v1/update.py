"""POST statuses/update API

タイムラインにツィートします。

https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update
"""

from shared_code.twitter.api.v1 import proxy

class Param(proxy.ParamInterface):
    """POST statuses/update API のパラメーター

    Attributes:
        _param: パラメーター
    """
    def __init__(self, status: str):
        """コンストラクタ

        Args:
            status: ツィートする文言
        """
        super().__init__()
        self._param = {
            'status': status
        }

    def get_endpoint_url(self) -> str:
        return 'https://api.twitter.com/1.1/statuses/update.json'

    def get_session(self) -> object:
        return self._session.post

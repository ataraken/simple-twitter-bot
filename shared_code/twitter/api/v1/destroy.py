"""POST statuses/destroy/:id

タイムライン上のツィートを削除するためのパラメーターを管理します。

https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-destroy-id

"""

from shared_code.twitter.api.v1 import proxy

class Param(proxy.ParamInterface):
    """statuses/destroy/:id のパラメーター

    Attributes:
        _tweet_id: 削除対象のツィートID
        _param: パラメーター
    """
    def __init__(self, id: int):
        """コンストラクタ

        Args:
            id: 削除するツィートのID
        """
        super().__init__()
        self._tweet_id = id
        self._param = {
            'trim_user': None
        }

    def get_tweet_id(self) -> int:
        """ツィートIDの取得

        Returns:
            ツィートID
        """
        return self._tweet_id

    def get_endpoint_url(self) -> str:
        """API の endpoint URL の取得

        Returns:
            endpoint URL
        """
        return f'https://api.twitter.com/1.1/statuses/destroy/{self.get_tweet_id()}.json'

    def get_session(self) -> object:
        """OAuth セッションの取得

        Returns
            OAuth セッション
        """
        return self._session.post


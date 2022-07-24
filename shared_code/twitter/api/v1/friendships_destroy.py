"""POST friendships/destroy API

friend を削除します。
フォローしているユーザーのフォローをやめることに相当します。

https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/follow-search-get-users/api-reference/post-friendships-destroy
"""

from shared_code.twitter.api.v1 import proxy

class Param(proxy.ParamInterface):
    """POST friendships/destroy API のパラメーター

    Attributes:
        _param: パラメーター
    """
    def __init__(self, user_id: int):
        """コンストラクタ

        Args:
            user_id: 削除する friend の ID
        """
        super().__init__()
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

    def get_session(self) -> object:
        return self._session.post
        

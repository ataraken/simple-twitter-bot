"""The proxy to the Twitter service.
"""
import json

from abc import ABC, abstractmethod
from typing import Any

from shared_code import twitter_oauth_helper

class ParamInterface(ABC):
    """ The Interface for parameter to use twitter API."""

    def __init__(self):
        self._session = twitter_oauth_helper.create_session()

    def convert_to_query(self) -> str:
        """パラメーターから Twitter API のクエリ文字列を生成

        Returns:
            クエリ文字列
        """
        return { k: self._param[k] for k in self._param if None != self._param[k] }

    @abstractmethod
    def get_endpoint_url(self) -> str:
        """Twitter API の endpoint URL を取得

        Returns:
            エンドポイント URL
        """
        pass

    @abstractmethod
    def get_session(self) -> object:
        """HTTPリクエストをするためのセッションを取得

        Returns:
            requests の get/post リクエスト
        """
        pass

def request(param: ParamInterface, session: Any) -> Any:
    """HTTP リクエストの実行

    Args:
        param: Twitter API のパラメーター
        session: Twitter API で使用する HTTP セッションの抽象

    Returns:
        レスポンス・ボディ
    """
    query = param.convert_to_query()

    if not query:
        res = session(param.get_endpoint_url())
    else:
        res = session(param.get_endpoint_url(), params=query)

    if res.status_code == 200:
        res = json.loads(res.text)
    else:
        raise RuntimeError('Network Error. status code: {res.status_code}')

    return res

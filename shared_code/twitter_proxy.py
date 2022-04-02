"""The proxy to the Twitter service.
"""
import json

from abc import ABC, abstractmethod
from typing import Any

from shared_code import twitter_oauth_helper

class ParamInterface(ABC):
    """ The Interface for parameter to use twitter API."""

    def convert_to_query(self) -> str:
        return { k: self._param[k] for k in self._param if None != self._param[k] }

    @abstractmethod
    def get_endpoint_url(self) -> str:
        pass

def get_get_session() -> Any:
    return twitter_oauth_helper.create_session().get

def get_post_session() -> Any:
    return twitter_oauth_helper.create_session().post

def request(param: ParamInterface, session: Any) -> str:
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

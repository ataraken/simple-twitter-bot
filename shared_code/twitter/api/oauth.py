"""Twitter API にアクセスするためのセッションを生成する

Twitter API にアクセスするための OAuth オブジェクトを生成する。
下記の環境変数を設定すること

TWITTER_ACCESS_TOKEN: Access token
TWITTER_TOKEN_SECRET: Access token secret
TWITTER_API_KEY: API Key
TWITTER_API_SECRET_KEY: API secret key
"""

from requests_oauthlib import OAuth1Session
from os import environ

def create_session() -> OAuth1Session:
    """Twitter API にアクセスするためのセッションを取得する

    Args:

    Returns:
        OAuth セッション

    Raise:
    """
    token = environ['TWITTER_ACCESS_TOKEN']
    token_secret = environ['TWITTER_TOKEN_SECRET']
    consumer_key = environ['TWITTER_API_KEY']
    consumer_secret = environ['TWITTER_API_SECRET_KEY']

    return OAuth1Session(consumer_key, consumer_secret, token, token_secret)

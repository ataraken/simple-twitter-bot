# <project_root>/shared_code/twitter_oauth_helper.py

from requests_oauthlib import OAuth1Session
from os import environ

def create_session() -> OAuth1Session:
    token = environ['TWITTER_ACCESS_TOKEN']
    token_secret = environ['TWITTER_TOKEN_SECRET']
    consumer_key = environ['TWITTER_API_KEY']
    consumer_secret = environ['TWITTER_API_SECRET_KEY']

    return OAuth1Session(consumer_key, consumer_secret, token, token_secret)

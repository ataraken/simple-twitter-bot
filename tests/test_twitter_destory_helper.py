"""The Unit Test for twitter_destory_helper.py
"""

import unittest
from unittest.mock import patch

import azure.functions as func
from shared_code import twitter_destroy_helper

class TestTwitterDestroyParam(unittest.TestCase):
    """Test class for Param class to use twitter destory API."""

    def test_constructor(self):
        param = twitter_destroy_helper.Param('tweet-id')
        self.assertEqual(param.get_tweet_id(), 'tweet-id')

    def test_endpoint_url(self):
        id = 'tweet-id'
        param = twitter_destroy_helper.Param(id)
        self.assertEqual(param.get_endpoint_url(), f'https://api.twitter.com/1.1/statuses/destroy/{id}.json')

if __name__ == '__main__':
    unittest.main()
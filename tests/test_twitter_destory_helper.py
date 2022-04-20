"""The Unit Test for twitter_destory_helper.py
"""

import unittest
from unittest.mock import patch

from shared_code import twitter_destroy_helper

class TestTwitterDestroyParam(unittest.TestCase):
    """Test class for Param class to use twitter destory API."""

    def test_constructor(self):
        param = twitter_destroy_helper.Param(12345)
        self.assertEqual(param.get_tweet_id(), 12345)

    def test_endpoint_url(self):
        id = 12345
        param = twitter_destroy_helper.Param(id)
        self.assertEqual(param.get_endpoint_url(), f'https://api.twitter.com/1.1/statuses/destroy/{id}.json')

    def test_endpoint_url2(self):
        id = 148215270139483904
        param = twitter_destroy_helper.Param(id)
        self.assertEqual(param.get_endpoint_url(), f'https://api.twitter.com/1.1/statuses/destroy/{id}.json')

if __name__ == '__main__':
    unittest.main()
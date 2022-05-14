"""The Unit Test for twitter_destory_helper.py
"""

import unittest
from unittest.mock import patch

from shared_code.twitter.api.v1 import destroy

class TestTwitterDestroyParam(unittest.TestCase):
    """Test class for Param class to use twitter destory API."""

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_constructor(self, mock):
        """コンストラクタのテスト
        """
        param = destroy.Param(12345)
        self.assertEqual(param.get_tweet_id(), 12345)

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_endpoint_url(self, mock):
        """endpoint URL のテスト
        """
        id = 12345
        param = destroy.Param(id)
        self.assertEqual(param.get_endpoint_url(), f'https://api.twitter.com/1.1/statuses/destroy/{id}.json')

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_endpoint_url2(self, mock):
        """endpoint URL のテスト
        """
        id = 148215270139483904
        param = destroy.Param(id)
        self.assertEqual(param.get_endpoint_url(), f'https://api.twitter.com/1.1/statuses/destroy/{id}.json')

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_get_session(self, mock):
        """セッションのテスト
        """
        param = destroy.Param(12345)
        self.assertEqual(param.get_session(), param._session.post)


if __name__ == '__main__':
    unittest.main()
"""The Unit Test for twitter_update_helper.py
"""

import unittest
from unittest.mock import patch

from shared_code import twitter_update_helper

class TestTwitterUpdateParam(unittest.TestCase):
    """Test class for Param class to use twitter update API."""

    @patch('shared_code.twitter_oauth_helper.create_session')
    def test_constructor(self, mock):
        param = twitter_update_helper.Param('text')
        self.assertEqual(param._param['status'], 'text')

    @patch('shared_code.twitter_oauth_helper.create_session')
    def test_endpoint_url(self, mock):
        param = twitter_update_helper.Param('text')
        self.assertEqual(param.get_endpoint_url(), 'https://api.twitter.com/1.1/statuses/update.json')

    @patch('shared_code.twitter_oauth_helper.create_session')
    def test_session(self, mock) -> None:
        param = twitter_update_helper.Param('text')
        self.assertEqual(param.get_session(), param._session.post)

if __name__ == '__main__':
    unittest.main()
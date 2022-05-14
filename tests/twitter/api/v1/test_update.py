"""The Unit Test for update.py
"""

import unittest
from unittest.mock import patch

from shared_code.twitter.api.v1 import update

class TestTwitterUpdateParam(unittest.TestCase):
    """Test class for Param class to use twitter update API."""

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_constructor(self, mock):
        param = update.Param('text')
        self.assertEqual(param._param['status'], 'text')

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_endpoint_url(self, mock):
        param = update.Param('text')
        self.assertEqual(param.get_endpoint_url(), 'https://api.twitter.com/1.1/statuses/update.json')

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_session(self, mock) -> None:
        param = update.Param('text')
        self.assertEqual(param.get_session(), param._session.post)

if __name__ == '__main__':
    unittest.main()
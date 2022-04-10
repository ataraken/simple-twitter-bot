"""The Unit Test for twitter_update_helper.py
"""

import unittest
from unittest.mock import patch

from shared_code import twitter_update_helper

class TestTwitterUpdateParam(unittest.TestCase):
    """Test class for Param class to use twitter update API."""

    def test_constructor(self):
        param = twitter_update_helper.Param('text')
        self.assertEqual(param._param['status'], 'text')

    def test_endpoint_url(self):
        param = twitter_update_helper.Param('text')
        self.assertEqual(param.get_endpoint_url(), 'https://api.twitter.com/1.1/statuses/update.json')

if __name__ == '__main__':
    unittest.main()
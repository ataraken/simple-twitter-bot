"""The Unit Test for twitter_aouth_helper.py
"""

import unittest
from unittest.mock import Mock
from unittest.mock import patch

from shared_code import twitter_oauth_helper

class TestTwitterAOuth(unittest.TestCase):
    """Test class for Param class to use twitter destory API."""

    @patch.dict('os.environ', 
        {'TWITTER_ACCESS_TOKEN': 'access-token',
        'TWITTER_TOKEN_SECRET': 'token-secret', 
        'TWITTER_API_KEY': 'api-key', 
        'TWITTER_API_SECRET_KEY': 'api-secret-key'})
    @patch('shared_code.twitter_oauth_helper.OAuth1Session')
    def test_create_session(self, mock):
        twitter_oauth_helper.create_session()
        mock.assert_called_once_with('api-key', 'api-secret-key', 'access-token', 'token-secret')

if __name__ == '__main__':
    unittest.main()
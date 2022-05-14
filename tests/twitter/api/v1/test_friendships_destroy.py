"""The Unit Test for twitter_friendships_destory_helper.py
"""

import unittest
from unittest.mock import patch

from shared_code.twitter.api.v1 import friendships_destroy

class TestTwitterFriendshipsDestroyParam(unittest.TestCase):
    """Test class for Param class to use twitter destory API."""

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_constructor(self, mock):
        id = 12345
        param = friendships_destroy.Param(id)
        self.assertEqual(param.get_user_id(), id)

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_user_id(self, mock):
        param = friendships_destroy.Param(9876)
        id = 123
        param.set_user_id(id)
        self.assertEqual(param.get_user_id(), id)

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_screen_name(self, mock):
        param = friendships_destroy.Param(9876)
        screen_name = 'name'
        param.set_screen_name(screen_name)
        self.assertEqual(param.get_screen_name(), screen_name)

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_endpoint_url(self, mock):
        param = friendships_destroy.Param(123)
        self.assertEqual(param.get_endpoint_url(), f'https://api.twitter.com/1.1/friendships/destroy.json')

    @patch('shared_code.twitter.api.oauth.create_session')
    def test_session(self, mock) -> None:
        param = friendships_destroy.Param(123)
        self.assertEqual(param.get_session(), param._session.post)

if __name__ == '__main__':
    unittest.main()
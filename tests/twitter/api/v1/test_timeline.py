"""Unit Test for timeline.py. 

"""

import unittest
from unittest.mock import patch

from shared_code.twitter.api.v1 import timeline

class TestTwitterTimelineParam(unittest.TestCase):
    """Unit Test for timeline.py"""

    @patch('shared_code.twitter.api.oauth.create_session')
    @patch.dict('os.environ', {'TWITTER_USER_ID': 'test-user-id'})
    def setUp(self, mock) -> None:
        self._param = timeline.Param()

    def tearDown(self) -> None:
        self._param = None

    def test_user_id_1(self) -> None:
        """Default user id test."""
        self.assertEqual(self._param.get_user_id(), 'test-user-id')

    def test_user_id_2(self) -> None:
        self._param.set_user_id('test2')
        self.assertEqual(self._param.get_user_id(), 'test2')

    def test_default_count(self) -> None:
        self.assertEqual(self._param.get_count(), None)

    def test_count1(self) -> None:
        self._param.set_count(123)
        self.assertEqual(self._param.get_count(), 123)

    def test_count2(self) -> None:
        self._param.set_count(-1)
        self.assertEqual(self._param.get_count(), 1)

    def test_count3(self) -> None:
        self._param.set_count(0)
        self.assertEqual(self._param.get_count(), 1)

    def test_count4(self) -> None:
        self._param.set_count(200)
        self.assertEqual(self._param.get_count(), 200)

    def test_count5(self) -> None:
        self._param.set_count(201)
        self.assertEqual(self._param.get_count(), 200)

    def test_count5(self) -> None:
        self._param.set_count(201)
        self.assertEqual(self._param.get_count(), 200)

    def test_max_id(self) -> None:
        self._param.set_max_id(123)
        self.assertEqual(self._param.get_max_id(), 123)

    def test_trim_user(self) -> None:
        self.assertEqual(self._param.get_trim_user(), None)

    def test_exclude_replies(self) -> None:
        self.assertEqual(self._param.get_exclude_replies(), None)

    def test_include_replies(self) -> None:
        self.assertEqual(self._param.get_include_entitles(), None)

    def test_tweet_mode(self) -> None:
        self.assertEqual(self._param.get_tweet_mode(), 'extended')

    def test_endpoint_url(self) -> None:
        self.assertEqual(self._param.get_endpoint_url(), 'https://api.twitter.com/1.1/statuses/user_timeline.json')

    def test_session(self) -> None:
        self.assertEqual(self._param.get_session(), self._param._session.get)

if __name__ == '__main__':
    unittest.main()
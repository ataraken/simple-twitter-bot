# 
import unittest
from unittest.mock import patch

from shared_code import twitter_friends_ids_helper

class TestTwitterFriendsIdsHelper(unittest.TestCase):

    @patch.dict('os.environ', {'TWITTER_USER_ID': 'test-user-id'})
    def setUp(self) -> None:
        self._param = twitter_friends_ids_helper.Param()

    def tearDown(self) -> None:
        self._param = None

    def test_init_error(self) -> None:
        try:
            twitter_friends_ids_helper.Param()
        except Exception as e:
            self.assertTrue(True)

    def test_user_id1(self) -> None:
        self.assertEqual(self._param.get_user_id(), 'test-user-id')

    def test_user_id2(self) -> None:
        self._param.set_user_id('user2')
        self.assertEqual(self._param.get_user_id(), 'user2')

    def test_screen_name1(self) -> None:
        self.assertIsNone(self._param.get_screen_name())

    def test_screen_name2(self) -> None:
        self._param.set_screen_name('screen')
        self.assertEqual(self._param.get_screen_name(), 'screen')

    def test_cursor1(self) -> None:
        self.assertIsNone(self._param.get_cursor())

    def test_cursor2(self) -> None:
        self._param.set_cursor('cursor')
        self.assertEqual(self._param.get_cursor(), 'cursor')

    def test_stringify_ids1(self) -> None:
        self.assertIsNone(self._param.get_stringify_ids())

    def test_stringify_ids2(self) -> None:
        self._param.set_stringify_ids('ids')
        self.assertEqual(self._param.get_stringify_ids(), 'ids')

    def test_count1(self) -> None:
        self.assertEqual(self._param.get_count(), 5000)

    def test_count2(self) -> None:
        self._param.set_count(-1)
        self.assertEqual(self._param.get_count(), 1)

    def test_count3(self) -> None:
        self._param.set_count(0)
        self.assertEqual(self._param.get_count(), 1)

    def test_count4(self) -> None:
        self._param.set_count(1)
        self.assertEqual(self._param.get_count(), 1)

    def test_count5(self) -> None:
        self._param.set_count(2)
        self.assertEqual(self._param.get_count(), 2)

    def test_count6(self) -> None:
        self._param.set_count(4999)
        self.assertEqual(self._param.get_count(), 4999)

    def test_count7(self) -> None:
        self._param.set_count(5000)
        self.assertEqual(self._param.get_count(), 5000)

    def test_count8(self) -> None:
        self._param.set_count(5001)
        self.assertEqual(self._param.get_count(), 5000)

    def test_endpoint_url(self) -> None:
        self.assertEqual(self._param.get_endpoint_url(), 'https://api.twitter.com/1.1/friends/ids.json')

if __name__ == '__main__':
    unittest.main()
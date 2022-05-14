"""Unit Test for get_oldest_timeline_tweet.py
"""

import unittest
from unittest.mock import Mock
from unittest.mock import patch

from shared_code.twitter import get_oldest_timeline_tweet

class TestGetOldestTimelineTweet(unittest.TestCase):
    """get_oldest_timeline_tweetに対するユニットテスト
    """

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @patch('shared_code.twitter.api.v1.twitter_timeline_helper.Param')
    @patch('shared_code.twitter.api.v1.twitter_proxy.request')
    def test_get1(self, request_mock, param_mock) -> None:
        """タイムライン取得が１回ですむ場合のテスト
        """
        request_mock.return_value = [ {'id': '123', 'full_text': 'text'} ]

        id, text = get_oldest_timeline_tweet.get()

        self.assertEqual(id, '123')
        self.assertEqual(text, 'text')

    @patch('shared_code.twitter.api.v1.twitter_timeline_helper.Param')
    @patch('shared_code.twitter.api.v1.twitter_proxy.request')
    def test_get2(self, request_mock, param_mock) -> None:
        """タイムライン取得が２回の場合のテスト
        """
        ret_val1 = [ {'id': str(i), 'full_text': f'text-{i}' } for i in range(200) ]
        ret_val2 = [ {'id': str(200 + i), 'full_text': f'text-{200 + i}' } for i in range(199) ]
        request_mock.side_effect = [ ret_val1, ret_val2 ]

        id, text = get_oldest_timeline_tweet.get()

        self.assertEqual(id, '398')
        self.assertEqual(text, 'text-398')
        self.assertEqual(request_mock.call_count, 2)

    @patch('shared_code.twitter.api.v1.twitter_timeline_helper.Param')
    @patch('shared_code.twitter.api.v1.twitter_proxy.request')
    def test_get3(self, request_mock, param_mock) -> None:
        """タイムライン取得が３回の場合のテスト
        """
        ret_val1 = [ {'id': str(i), 'full_text': f'text-{i}' } for i in range(200) ]
        ret_val2 = [ {'id': str(200 + i), 'full_text': f'text-{200 + i}' } for i in range(200) ]
        ret_val3 = [ {'id': str(400 + i), 'full_text': f'text-{400 + i}' } for i in range(199) ]
        request_mock.side_effect = [ ret_val1, ret_val2, ret_val3 ]

        id, text = get_oldest_timeline_tweet.get()

        self.assertEqual(id, '598')
        self.assertEqual(text, 'text-598')
        self.assertEqual(request_mock.call_count, 3)

    @patch('shared_code.twitter.api.v1.twitter_timeline_helper.Param')
    @patch('shared_code.twitter.api.v1.twitter_proxy.request')
    def test_error(self, request_mock, param_mock) -> None:
        """エラーが発生する場合のテスト
        """
        request_mock.side_effect = RuntimeError('Test Error.')

        try:
            get_oldest_timeline_tweet.get()
        except RuntimeError:
            self.assertEqual(request_mock.call_count, 1)
            self.assertTrue(True)
        except:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
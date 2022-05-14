# 
import unittest
from unittest.mock import Mock
from unittest.mock import patch

import timer_trigger_tweet

class TestTimerTriggerTweet(unittest.TestCase):

    class TimerMock:
        def __init__(self):
            self.past_due = True

    @patch('shared_code.twitter.api.v1.twitter_destroy_helper.Param')
    @patch('shared_code.twitter.api.v1.twitter_proxy.request')
    @patch('shared_code.twitter.api.v1.twitter_update_helper.Param')
    @patch('shared_code.twitter.get_oldest_timeline_tweet.get')
    def test_get(self, oldest_mock, update_mock, proxy_mock, destroy_mock):
        oldest_mock.return_value = '123', 'text'
        update_mock.return_value = Mock()
        destroy_mock.return_value = Mock()

        timer_trigger_tweet.main(TestTimerTriggerTweet.TimerMock())

        self.assertEqual(oldest_mock.call_count, 1)
        self.assertEqual(update_mock.call_count, 1)
        self.assertEqual(destroy_mock.call_count, 1)
        self.assertEqual(proxy_mock.call_count, 2)

    @patch('shared_code.twitter.api.v1.twitter_destroy_helper.Param')
    @patch('shared_code.twitter.api.v1.twitter_proxy.request')
    @patch('shared_code.twitter.api.v1.twitter_update_helper.Param')
    @patch('shared_code.twitter.get_oldest_timeline_tweet.get')
    def test_error1(self, oldest_mock, update_mock, proxy_mock, sdestroy_mock):
        oldest_mock.side_effect = RuntimeError('Test Error.')

        timer_trigger_tweet.main(TestTimerTriggerTweet.TimerMock())

        self.assertTrue(True)

    @patch('shared_code.twitter.api.v1.twitter_destroy_helper.Param')
    @patch('shared_code.twitter.api.v1.twitter_proxy.request')
    @patch('shared_code.twitter.api.v1.twitter_update_helper.Param')
    @patch('shared_code.twitter.get_oldest_timeline_tweet.get')
    def test_error2(self, oldest_mock, update_mock, proxy_mock, destroy_mock):
        oldest_mock.return_value = '123', 'text'
        update_mock.return_value = Mock()
        proxy_mock.side_effect = RuntimeError('Test Error.')

        timer_trigger_tweet.main(TestTimerTriggerTweet.TimerMock())

        self.assertEqual(oldest_mock.call_count, 1)
        self.assertEqual(update_mock.call_count, 1)
        self.assertEqual(destroy_mock.call_count, 0)

    @patch('shared_code.twitter.api.v1.twitter_destroy_helper.Param')
    @patch('shared_code.twitter.api.v1.twitter_proxy.request')
    @patch('shared_code.twitter.api.v1.twitter_update_helper.Param')
    @patch('shared_code.twitter.get_oldest_timeline_tweet.get')
    def test_error3(self, oldest_mock, update_mock, proxy_mock, destroy_mock):
        oldest_mock.return_value = '123', 'text'
        update_mock.return_value = Mock()
        proxy_mock.side_effect = [ True, RuntimeError('Test Error.') ]

        timer_trigger_tweet.main(TestTimerTriggerTweet.TimerMock())

        self.assertEqual(oldest_mock.call_count, 1)
        self.assertEqual(update_mock.call_count, 1)
        self.assertEqual(proxy_mock.call_count, 2)
        self.assertEqual(destroy_mock.call_count, 1)

if __name__ == '__main__':
    unittest.main()
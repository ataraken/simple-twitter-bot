# 
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import call

import timer_trigger_remove_back_followers

class TestTimerTriggerRemoveBackFollowers(unittest.TestCase):
    class TimerMock:
        def __init__(self):
            self.past_due = True

    def init_mocks(self, friends_mock, followers_mock, destroy_mock, request_mock):
        friends_mock.return_value = Mock()
        followers_mock.return_value = Mock()
        destroy_mock.return_value = Mock()
        request_mock.side_effect = None        

    @patch('shared_code.twitter_proxy.request')
    @patch('shared_code.twitter_friendships_destroy_helper.Param')
    @patch('shared_code.twitter_followers_ids_helper.Param')
    @patch('shared_code.twitter_friends_ids_helper.Param')
    def test1(self, friends_mock, followers_mock, destroy_mock, request_mock):
        self.init_mocks(friends_mock, followers_mock, destroy_mock, request_mock)
        request_mock.side_effect = [ { 'ids': [1, 2, 3, 4] }, { 'ids': [1, 3] }, True, True]

        timer_trigger_remove_back_followers.main(TestTimerTriggerRemoveBackFollowers.TimerMock())

        self.assertEqual(destroy_mock.call_args_list, [call(2), call(4)])

    @patch('shared_code.twitter_proxy.request')
    @patch('shared_code.twitter_friendships_destroy_helper.Param')
    @patch('shared_code.twitter_followers_ids_helper.Param')
    @patch('shared_code.twitter_friends_ids_helper.Param')
    def test2(self, friends_mock, followers_mock, destroy_mock, request_mock):
        self.init_mocks(friends_mock, followers_mock, destroy_mock, request_mock)
        request_mock.side_effect = [ { 'ids': [1, 2, 3, 4, 5, 6] }, { 'ids': [1, 4] }, True, True, True, True]

        timer_trigger_remove_back_followers.main(TestTimerTriggerRemoveBackFollowers.TimerMock())

        self.assertEqual(destroy_mock.call_args_list, [call(2), call(3), call(5), call(6)])

    @patch('shared_code.twitter_proxy.request')
    @patch('shared_code.twitter_friendships_destroy_helper.Param')
    @patch('shared_code.twitter_followers_ids_helper.Param')
    @patch('shared_code.twitter_friends_ids_helper.Param')
    def test3(self, friends_mock, followers_mock, destroy_mock, request_mock):
        self.init_mocks(friends_mock, followers_mock, destroy_mock, request_mock)
        request_mock.side_effect = [ { 'ids': [1, 2] }, { 'ids': [1, 2] }]

        timer_trigger_remove_back_followers.main(TestTimerTriggerRemoveBackFollowers.TimerMock())

        self.assertFalse(destroy_mock.called)

    @patch('shared_code.twitter_proxy.request')
    @patch('shared_code.twitter_friendships_destroy_helper.Param')
    @patch('shared_code.twitter_followers_ids_helper.Param')
    @patch('shared_code.twitter_friends_ids_helper.Param')
    def test_error1(self, friends_mock, followers_mock, destroy_mock, request_mock):
        self.init_mocks(friends_mock, followers_mock, destroy_mock, request_mock)
        request_mock.side_effect = [RuntimeError('Test Error.')]

        timer_trigger_remove_back_followers.main(TestTimerTriggerRemoveBackFollowers.TimerMock())

        self.assertTrue(friends_mock.called)
        self.assertFalse(followers_mock.called)
        self.assertFalse(destroy_mock.called)

    @patch('shared_code.twitter_proxy.request')
    @patch('shared_code.twitter_friendships_destroy_helper.Param')
    @patch('shared_code.twitter_followers_ids_helper.Param')
    @patch('shared_code.twitter_friends_ids_helper.Param')
    def test_error2(self, friends_mock, followers_mock, destroy_mock, request_mock):
        self.init_mocks(friends_mock, followers_mock, destroy_mock, request_mock)
        request_mock.side_effect = [ True, RuntimeError('Test Error.')]

        timer_trigger_remove_back_followers.main(TestTimerTriggerRemoveBackFollowers.TimerMock())

        self.assertTrue(friends_mock.called)
        self.assertTrue(followers_mock.called)
        self.assertFalse(destroy_mock.called)

    @patch('shared_code.twitter_proxy.request')
    @patch('shared_code.twitter_friendships_destroy_helper.Param')
    @patch('shared_code.twitter_followers_ids_helper.Param')
    @patch('shared_code.twitter_friends_ids_helper.Param')
    def test_error3(self, friends_mock, followers_mock, destroy_mock, request_mock):
        self.init_mocks(friends_mock, followers_mock, destroy_mock, request_mock)
        request_mock.side_effect = [ { 'ids': [1, 2] }, { 'ids': [1] }, RuntimeError('Test Error.')]

        timer_trigger_remove_back_followers.main(TestTimerTriggerRemoveBackFollowers.TimerMock())

        self.assertTrue(friends_mock.called)
        self.assertTrue(followers_mock.called)
        self.assertTrue(destroy_mock.called)

    @patch('shared_code.twitter_proxy.request')
    @patch('shared_code.twitter_friendships_destroy_helper.Param')
    @patch('shared_code.twitter_followers_ids_helper.Param')
    @patch('shared_code.twitter_friends_ids_helper.Param')
    def test_error4(self, friends_mock, followers_mock, destroy_mock, request_mock):
        self.init_mocks(friends_mock, followers_mock, destroy_mock, request_mock)
        request_mock.side_effect = [ { 'ids': [1, 2, 3] }, { 'ids': [1] }, True, RuntimeError('Test Error.')]

        timer_trigger_remove_back_followers.main(TestTimerTriggerRemoveBackFollowers.TimerMock())

        self.assertTrue(friends_mock.called)
        self.assertTrue(followers_mock.called)
        self.assertTrue(destroy_mock.called)
        self.assertEqual(destroy_mock.call_count, 2)

if __name__ == '__main__':
    unittest.main()
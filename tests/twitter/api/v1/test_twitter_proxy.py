"""The Unit Test for twitter_proxy.py
"""

import unittest
from unittest.mock import Mock
from unittest.mock import patch

import shared_code
from shared_code.twitter.api.v1 import twitter_proxy

class TestTwitterProxy(unittest.TestCase):
    """Unit Test for twitter_proxy.py."""

    class TestParam(twitter_proxy.ParamInterface):
        """Mock Class"""
        def __init__(self) -> None:
            super().__init__()
            self._param = {
                'key1': 'value1',
                'key2': 'value2'
            }
           
        def get_endpoint_url(self) -> str:
            return 'https://test.com'

        def get_session(self) -> object:
            return None

    @patch('shared_code.twitter.api.twitter_oauth_helper.create_session')
    def setUp(self, mock):
        self._param = TestTwitterProxy.TestParam()

    def tearDown(self):
        self._param = None

    def test_query1(self):
        self._param._param = {}
        self.assertFalse(self._param.convert_to_query())

    def test_query2(self):
        self._param._param['key1'] = None
        self._param._param['key2'] = None
        self.assertFalse(self._param.convert_to_query())

    def test_query3(self):
        self._param._param['key2'] = None
        self.assertEqual(self._param.convert_to_query(), {'key1': 'value1'})

    def test_query4(self):
        self._param._param['key1'] = None
        self.assertEqual(self._param.convert_to_query(), {'key2': 'value2'})

    def test_query5(self):
        self.assertEqual(self._param.convert_to_query(), {'key1': 'value1', 'key2': 'value2'})

    def test_query6(self):
        self._param._param['key3'] = 'value3'
        self.assertEqual(self._param.convert_to_query(), {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})

    def test_query7(self):
        self._param._param['key1'] = 'test7'
        self.assertEqual(self._param.convert_to_query(), {'key1': 'test7', 'key2': 'value2'})

    def test_request1(self):
        response_mock = Mock()
        response_mock.configure_mock(status_code=200)
        response_mock.configure_mock(text='{"key": "value"}')

        session_mock = Mock()
        session_mock.return_value = response_mock

        res = twitter_proxy.request(self._param, session_mock)

        session_mock.assert_called_once_with(self._param.get_endpoint_url(), params=self._param.convert_to_query())
        self.assertEqual(res['key'], 'value')

    def test_request2(self):
        self._param._param = {}

        response_mock = Mock()
        response_mock.configure_mock(status_code=200)
        response_mock.configure_mock(text='{"key": "value"}')

        session_mock = Mock()
        session_mock.return_value = response_mock

        res = twitter_proxy.request(self._param, session_mock)

        session_mock.assert_called_once_with(self._param.get_endpoint_url())
        self.assertEqual(res['key'], 'value')

    def test_request3(self):
        response_mock = Mock()
        response_mock.configure_mock(status_code=404)

        session_mock = Mock()
        session_mock.return_value = response_mock

        try:
            twitter_proxy.request(self._param, session_mock)
        except RuntimeError:
            response_mock.called
            self.assertTrue(True)
            return
        except:
            pass
        self.assertTrue(False)

    def test_request4(self):
        response_mock = Mock()
        response_mock.configure_mock(status_code=201)

        session_mock = Mock()
        session_mock.return_value = response_mock

        try:
            twitter_proxy.request(self._param, session_mock)
        except RuntimeError:
            session_mock.called
            self.assertTrue(True)
            return
        except:
            pass
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()
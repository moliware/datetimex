import datetimex
import pytz
import unittest

from datetime import datetime
from freezegun import freeze_time


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # TODO:
    # @freeze_time('2014-05-05 03:21:34')
    # def test_now_timezones(self):
    #     expected = datetime.now(pytz.timezone('US/Eastern'))
    #     self.assertEqual(datetimex.now(pytz.timezone('US/Eastern')), expected)
    #     self.assertEqual(datetimex.now('US/Eastern'), expected)


if __name__ == '__main__':
    unittest.main()
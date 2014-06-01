import datetimex
import unittest

from datetime import datetime
from freezegun import freeze_time


class DatesTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @freeze_time("2014-05-18")
    def test_ago(self):
        self.assertEqual((1).days.ago, datetime(2014, 5, 17))

    @freeze_time("2014-05-18")
    def test_since(self):
        self.assertEqual((2).days.since(datetime.now()), datetime(2014, 5, 20))

import datetimex
import unittest

from datetime import timedelta


class DurationsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_micros(self):
        self.assertEqual((1).micros, timedelta(microseconds=1))

    def test_microseconds(self):
        self.assertEqual((1).microseconds, timedelta(microseconds=1))

    def test_millis(self):
        self.assertEqual((1).millis, timedelta(milliseconds=1))

    def test_milliseconds(self):
        self.assertEqual((1).milliseconds, timedelta(milliseconds=1))

    def test_secs(self):
        self.assertEqual((1).secs, timedelta(seconds=1))

    def test_seconds(self):
        self.assertEqual((1).seconds, timedelta(seconds=1))

    def test_mins(self):
        self.assertEqual((1).mins, timedelta(minutes=1))

    def test_minutes(self):
        self.assertEqual((1).minutes, timedelta(minutes=1))

    def test_hours(self):
        self.assertEqual((1).hours, timedelta(hours=1))

    def test_days(self):
        self.assertEqual((1).days, timedelta(days=1))

    def test_weeks(self):
        self.assertEqual((1).weeks, timedelta(weeks=1))

    def test_years(self):
        self.assertEqual((1).years, timedelta(days=365))
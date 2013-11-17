from unittest import TestCase
from Timer import Timer
import time

__author__ = 'Alexandre Cloquet'
__credits__ = ["Alexandre Cloquet"]
__version__ = "0.1"
__maintainer__ = "Alexandre Cloquet"
__email__ = "Alexandre.cloquet@gmail.com"
__status__ = "Development"


class TestTimer(TestCase):
    timer = Timer()

    def setUp(self):
        self.timer.begin_bot()
        time.sleep(90)

    def test_begin_bot(self):
        """
        Can't be tested
        """
        pass

    def test_end_bot(self):
        """
        Can't be tested
        """
        pass

    def test_get_minutes(self):
        self.timer.end_bot()
        self.assertEqual(self.timer.get_minutes(), 1)

    def test_get_hours(self):
        self.timer.end_bot()
        self.assertEqual(self.timer.get_hours(), 0)

    def test_get_seconds(self):
        self.timer.end_bot()
        self.assertAlmostEquals(self.timer.get_seconds(), 30, delta=1)

    def test_get_day(self):
        self.timer.end_bot()
        self.assertEqual(self.timer.get_day(), 0)

    def test_get_days_hours_minutes(self):
        self.timer.end_bot()
        assert self.timer.get_days_hours_minutes() == (0, 0, 1)

    def test_get_all_seconds(self):
        self.timer.end_bot()
        assert self.timer.get_all_seconds() == 90
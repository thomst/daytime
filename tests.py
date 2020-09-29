import unittest
from datetime import datetime
from datetime import timedelta
from datetime import time
from datetime import tzinfo
from daytime import Daytime


class UTC(tzinfo):
    def utcoffset(self, dt):
        return timedelta(0)

    def dst(self, dt):
        return timedelta(0)


class DayTimeTest(unittest.TestCase):
    def setUp(self):
        self.daytime1 = Daytime.fromtime(time(0, 0, 0, 8000))
        self.daytime2 = Daytime.strptime('2,20,22,007000', '%H,%M,%S,%f')
        self.daytime3 = Daytime.utcfromtimestamp(Daytime(2, 20, 23, 90000).as_seconds)
        self.daytime4 = Daytime.fromtimestamp(Daytime(12, 25, 0, 8400).as_seconds, UTC())
        self.daytime5 = Daytime(18, 43, 20, 6000)
        self.daytime6 = Daytime.daytime

    def test_comparison(self):
        self.assertTrue(self.daytime1 < self.daytime3 > self.daytime2)
        self.assertTrue(self.daytime1 < 20 < self.daytime2)
        self.assertTrue(self.daytime4 <= self.daytime4 >= self.daytime3)
        self.assertTrue(self.daytime4 <= self.daytime4.as_seconds >= self.daytime3)
        self.assertEqual(self.daytime4, self.daytime4)
        self.assertEqual(self.daytime4, self.daytime4.as_seconds)
        self.assertNotEqual(self.daytime4, self.daytime3)
        self.assertNotEqual(self.daytime4, self.daytime3.as_seconds)
        self.assertEqual(self.daytime4, time(12, 25, 0, 8400))

    def test_addition(self):
        self.assertTrue(self.daytime2 + self.daytime3 == time(4,40,45,97000))
        self.assertTrue(self.daytime2 - self.daytime3 == time(23,59,58,917000))
        self.assertTrue(self.daytime2 + time(1,2,3,4) == time(3,22,25,7004))
        self.assertTrue(self.daytime5 + 4 == time(18, 43, 24, 6000))
        self.assertTrue(self.daytime5 + timedelta(hours=10) == time(4, 43, 20, 6000))


if __name__ == '__main__':
    unittest.main()

import unittest
from datetime import datetime
from datetime import time
from daytime import DayTime

class DayTimeTest(unittest.TestCase):
    def setUp(self):
        self.daytime1 = DayTime(0, 0, 0, 8000)
        self.daytime2 = DayTime(2, 20, 22, 7000)
        self.daytime3 = DayTime(2, 20, 23, 90000)
        self.daytime4 = DayTime(12, 25, 0, 8400)
        self.daytime5 = DayTime(18, 43, 20, 6000)

    def test_comparison(self):
        self.assertTrue(self.daytime1 < self.daytime3 > self.daytime2)
        self.assertTrue(self.daytime4 <= self.daytime4 >= self.daytime3)
        self.assertEqual(self.daytime4, self.daytime4)
        self.assertTrue(self.daytime3.as_seconds < self.daytime4 <= self.daytime5.as_seconds)
        self.assertEqual(self.daytime4, time(12, 25, 0, 8400))

    def test_addition(self):
        self.assertTrue(self.daytime2 + self.daytime3 == time(4,40,45,97000))
        self.assertTrue(self.daytime2 - self.daytime3 == time(23,59,58,917000))
        self.assertTrue(self.daytime2 + time(1,2,3,4) == time(3,22,25,7004))


if __name__ == '__main__':
    unittest.main()

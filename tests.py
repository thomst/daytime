import unittest
from datetime import datetime
from datetime import time
from daytime import DayTime

class DayTimeTest(unittest.TestCase):
    def setUp(self):
        self.daytime1 = DayTime(0, 0, 0)
        self.daytime2 = DayTime(2, 20, 22)
        self.daytime3 = DayTime(2, 20, 23)
        self.daytime4 = DayTime(12, 25, 0)
        self.daytime5 = DayTime(18, 43, 20)

    def test_comparison(self):
        self.assertTrue(self.daytime1 < self.daytime3 > self.daytime2)
        self.assertTrue(self.daytime4 <= self.daytime4 >= self.daytime3)
        self.assertEqual(self.daytime4, self.daytime4)
        self.assertTrue(self.daytime3.total_seconds < self.daytime4 <= self.daytime5.total_seconds)

    def test_addition(self):
        self.assertTrue(self.daytime2 + self.daytime3 == time(4,40,45))
        self.assertTrue(self.daytime2 - self.daytime3 == time(23,59,59))


if __name__ == '__main__':
    unittest.main()

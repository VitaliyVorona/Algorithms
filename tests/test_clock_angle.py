import unittest
from checkio import Clock_Angle
from checkio import *


class TestClockAngle(unittest.TestCase):
    def test_180_angle(self):
        Clock_Angle.clock_angle('20:30')

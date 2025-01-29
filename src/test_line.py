import unittest
from line import Line
from point import Point

class TestLine(unittest.TestCase):
    def test_def(self):
        line = Line(Point(0,0), Point(1,1))
        self.assertEqual(line.p1, Point(0,0))
        self.assertEqual(line.p2, Point(1,1))

    def test_eq(self):
        point_a = Point(0,1)
        point_b = Point(1,0)
        point_c = Point(2,5)
        point_d = Point(5,5)
        line_a = Line(point_a, point_b)
        line_b = Line(point_b, point_a)
        line_c = Line(point_a, point_b)
        line_d = Line(point_c, point_d)
        line_e = Line(point_a, point_d)
        self.assertEqual(line_a, Line(point_a, point_b))
        self.assertEqual(line_a, line_b)
        self.assertEqual(line_a, line_c)
        self.assertNotEqual(line_d, line_e)

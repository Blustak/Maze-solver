import unittest
from cell import Cell

class TestCell(unittest.TestCase):
    def test_definition(self):
        cell = Cell(0,0,1,1, None)
        self.assertEqual(cell.walls, (False, False, False, False))
        self.assertEqual(cell._x1, 0)
        self.assertEqual(cell._y1, 0)
        self.assertEqual(cell._x2, 1)
        self.assertEqual(cell._y2, 1)
        self.assertIsNone(cell._win)

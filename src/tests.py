import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_empty(self):
        num_cols = 0
        num_rows = 0

        def new_maze():
            _ = Maze(0, 0, num_cols, num_rows, 10, 10)

        self.assertRaises(AssertionError, new_maze)

    def test_maze_1_row(self):
        num_cols = 10
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_1_col(self):
        num_rows = 10
        num_cols = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_exit(self):
        num_rows = 10
        num_cols = 10
        m1 = Maze(5, 5, num_rows, num_cols, 10, 10, seed=0)
        m2 = Maze(5, 5, num_rows, num_cols, 10, 10)
        self.assertTrue(
            m1._cells[0][0].has_top_wall is False
            and m1._cells[-1][-1].has_bottom_wall is False
        )
        self.assertTrue(
            m2._cells[0][0].has_top_wall is False
            and m2._cells[-1][-1].has_bottom_wall is False
        )


if __name__ == "__main__":
    unittest.main()

from typing import List
from cell import Cell
from point import Point
from window import Window
import time


class Maze:

    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        if win is None:
            print(
                """
                WARNING!
                Not drawing to a window. You should be in testing mode 
                for this.
                """
            )

    def _create_cells(self):
        self._cells: List[List[Cell]] = []
        for x in range(self._num_cols):
            col = []
            for y in range(self._num_rows):
                col.append(
                    Cell(
                        Point(
                            self._x1 + x * self._cell_size_x,
                            self._y1 + y * self._cell_size_y,
                        ),
                        self._cell_size_y,
                        self._cell_size_x,
                        self._win,
                    )
                )
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)

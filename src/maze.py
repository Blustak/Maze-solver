from cell import Cell
import time

REDRAW_PERIOD = 0.05

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y,
                 win,):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [[
            Cell(
                0,0,0,0, self._win, True, True, True, True,
        ) for _ in range(self._num_rows)] for _ in range(self._num_cols)]
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cells(i,j)
    def _draw_cells(self, i, j):
        cell:Cell = self._cells[i][j]
        cell._x1 = self._x1 + (j * self._cell_size_x)
        cell._x2 = cell._x1 + self._cell_size_x
        cell._y1 = self._y1 + (i * self._cell_size_y)
        cell._y2 = cell._y1 + self._cell_size_y
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(REDRAW_PERIOD)

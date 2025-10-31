from typing import List
from cell import Cell, WallType
from point import Point
import time
import random


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
        seed=None,
    ):
        assert num_rows > 0
        assert num_cols > 0
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if win is None:
            print(
                """
                WARNING!
                Not drawing to a window. You should be in testing mode 
                for this.
                """
            )

        random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        print(f"At cell {i}, {j}")
        self._animate()
        cell: Cell = self._cells[i][j]
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[i]) - 1:
            print(f"At the end. Returning true...")
            return True
        for dx, dy, wall in (
            (-1, 0, WallType.LEFT),
            (1, 0, WallType.RIGHT),
            (0, -1, WallType.TOP),
            (0, 1, WallType.BOTTOM),
        ):
            i_other = i + dx
            j_other = j + dy
            print(f"Searching {wall} ({i_other}, {j_other})")

            if i_other in range(len(self._cells)) and j_other in range(
                len(self._cells[i_other])
            ):
                cell_other = self._cells[i_other][j_other]
                if not cell.has_wall(wall) and not cell_other.visited:
                    cell.draw_move(
                        cell_other,
                        self._get_cell_origin(i, j),
                        self._get_cell_origin(i_other, j_other),
                        self._cell_size_x,
                        self._cell_size_y,
                    )
                    if self._solve_r(i_other, j_other):
                        return True
                    else:
                        cell.draw_move(
                            cell_other,
                            self._get_cell_origin(i, j),
                            self._get_cell_origin(i_other, j_other),
                            self._cell_size_x,
                            self._cell_size_y,
                            undo=True,
                        )
        return False

    def _create_cells(self):
        self._cells: List[List[Cell]] = []
        for x in range(self._num_cols):
            col = []
            for y in range(self._num_rows):
                col.append(
                    Cell(
                        Point(x, y),
                        self._win,
                    )
                )
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_wall(self, i: int, j: int, wall: WallType):
        self._cells[i][j].set_wall(wall, False)
        self._draw_cell(i, j)

    def _break_walls_r(self, i, j):
        to_visit = []
        self._cells[i][j].visited = True
        can_traverse = True
        while can_traverse:
            can_traverse = False
            if i > 0 and not self._cells[i - 1][j].visited:
                # There are cells to our left
                to_visit.append(((WallType.LEFT, WallType.RIGHT), (i - 1, j)))
            if j > 0 and not self._cells[i][j - 1].visited:
                # There are cells above us
                to_visit.append(((WallType.TOP, WallType.BOTTOM), (i, j - 1)))
            if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited:
                # This means there are cells to our right
                to_visit.append(((WallType.RIGHT, WallType.LEFT), (i + 1, j)))
            if (
                j < len(self._cells[i]) - 1
                and not self._cells[i][j + 1].visited
            ):
                # This means there are cells below us
                to_visit.append(((WallType.BOTTOM, WallType.TOP), (i, j + 1)))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                (walls_to_destroy, next_coord) = random.choice(to_visit)
                self._break_wall(
                    i,
                    j,
                    walls_to_destroy[0],
                )
                self._break_wall(
                    next_coord[0],
                    next_coord[1],
                    walls_to_destroy[1],
                )
                self._break_walls_r(next_coord[0], next_coord[1])

    def _break_entrance_and_exit(self):
        self._break_wall(0, 0, WallType.TOP)  # entrance
        self._break_wall(
            self._num_cols - 1, self._num_rows - 1, WallType.BOTTOM
        )

    def _reset_cells_visited(self):
        for x in self._cells:
            for cell in x:
                cell.visited = False

    def _draw_cell(self, i: int, j: int):
        o = self._get_cell_origin(i, j)
        x, y = o.x, o.y
        cell = self._cells[i][j]
        cell.draw(x, y, self._cell_size_x, self._cell_size_y)
        self._animate()

    def _get_cell_origin(self, i, j) -> Point:
        x = self._x1 + (i * self._cell_size_x)
        y = self._y1 + (j * self._cell_size_y)
        return Point(x, y)

    def _animate(self):
        if self._win:
            self._win.redraw()
            time.sleep(0.05)

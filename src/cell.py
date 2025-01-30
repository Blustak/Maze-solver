from point import Point
from line import Line
from window import Window

CELL_COLOR = "blue"
UNDO_COLOR = "red"
SOLVE_COLOR = "green"

class Cell:
    def __init__(self, x1, y1, x2, y2, window:Window, left_wall=False, right_wall=False, top_wall =
                 False, bottom_wall=False,):

        self.has_left_wall=left_wall
        self.has_top_wall = top_wall
        self.has_right_wall = right_wall
        self.has_bottom_wall = bottom_wall
        (self._x1, self._x2) = (x1, x2) if x1 < x2 else (x2, x1)
        self._y1, self._y2 = (y1, y2) if y1 < y2 else (y2, y1)
        self._win = window

    def draw(self):
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)
        if self.has_left_wall:
            left_wall = Line(top_left, Point(self._x1, self._y2))
            self._win.draw_line(left_wall, CELL_COLOR)
        if self.has_right_wall:
            right_wall = Line(bottom_right, Point(self._x2, self._y1))
            self._win.draw_line(right_wall, CELL_COLOR)
        if self.has_bottom_wall:
            bottom_wall = Line(bottom_right, Point(self._x1, self._y2))
            self._win.draw_line(bottom_wall, CELL_COLOR)
        if self.has_top_wall:
            top_wall = Line(top_left, Point(self._x2, self._y1))
            self._win.draw_line(top_wall, CELL_COLOR)

    def draw_move(self, to_cell, undo=False):
        line_color = UNDO_COLOR if undo else SOLVE_COLOR
        line = Line(self.get_center(), to_cell.get_center())
        self._win.draw_line(line, line_color)


    def get_center(self) -> Point:
        return Point((self._x1 + self._x2) //2, (self._y1 + self._y2) //2)

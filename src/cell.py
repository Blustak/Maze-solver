from point import Point
from line import Line
from window import Window

CELL_WIDTH = 50
CELL_HEIGHT = 50
CELL_COLOR = "black"

class Cell:
    def __init__(self, x, y, window:Window, left_wall=False, right_wall=False, top_wall =
                 False, bottom_wall=False,):

        self.has_left_wall=left_wall
        self.has_top_wall = top_wall
        self.has_right_wall = right_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = x * CELL_WIDTH # Top left corner
        self._x2 = (x+1) * CELL_WIDTH # Bottom right corner
        self._y1 = (y+1) * CELL_HEIGHT # Top left
        self._y2 = y * CELL_HEIGHT # Bottom right
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

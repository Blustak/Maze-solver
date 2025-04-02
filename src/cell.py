from point import Point
from line import Line
from window import Window
from enum import Enum, StrEnum, auto


class CellColor(StrEnum):
    EMPTY = "white"
    WALL = "black"
    PATH = "red"
    UNDO = "grey"


class WallType(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()


class Cell:
    def __init__(
        self, origin: Point, height: int, width: int, window: Window | None
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_top_wall = True
        self._x1 = origin.x
        self._y1 = origin.y
        self._x2 = origin.x + width
        self._y2 = origin.y + height
        self._win = window
        self.visited = False

    def draw(self):
        if not self._win:
            return
        top_left = Point(self._x1, self._y1)
        bottom_right = Point(self._x2, self._y2)
        bottom_left = Point(self._x1, self._y2)
        top_right = Point(self._x2, self._y1)

        left_wall = Line(top_left, bottom_left)
        right_wall = Line(top_right, bottom_right)
        top_wall = Line(top_left, top_right)
        bottom_wall = Line(bottom_left, bottom_right)

        canvas = self._win.canvas
        left_wall.draw(
            canvas,
            (CellColor.WALL if self.has_left_wall else CellColor.EMPTY),
        )

        right_wall.draw(
            canvas,
            (CellColor.WALL if self.has_right_wall else CellColor.EMPTY),
        )

        top_wall.draw(
            canvas,
            (CellColor.WALL if self.has_top_wall else CellColor.EMPTY),
        )

        bottom_wall.draw(
            canvas,
            (CellColor.WALL if self.has_bottom_wall else CellColor.EMPTY),
        )

    def draw_move(self, other, undo=False):
        if not self._win:
            return
        path = Line(self.get_center(), other.get_center())
        color = CellColor.PATH if undo else CellColor.UNDO
        path.draw(self._win.canvas, color)

    def get_center(self) -> Point:
        return Point(
            self._x1 + ((self._x2 - self._x1) / 2),
            self._y1 + ((self._y2 - self._y1) / 2),
        )

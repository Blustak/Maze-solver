from point import Point
from line import Line
from window import Window, ColorType
from enum import Enum, auto


class WallType(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()


class Cell:
    def __init__(self, origin: Point, window: Window | None):
        self._has_left_wall = True
        self._has_right_wall = True
        self._has_bottom_wall = True
        self._has_top_wall = True
        self._x1 = origin.x
        self._y1 = origin.y
        self._win = window
        self.visited = False

    def has_wall(self, wall: WallType):
        match wall:
            case WallType.LEFT:
                return self._has_left_wall
            case WallType.RIGHT:
                return self._has_right_wall
            case WallType.TOP:
                return self._has_top_wall
            case WallType.BOTTOM:
                return self._has_bottom_wall

    def draw(self, x, y, cell_width, cell_height):
        if not self._win:
            return
        top_left = Point(x, y)
        bottom_right = Point(x + cell_width, y + cell_height)
        bottom_left = Point(x, y + cell_height)
        top_right = Point(x + cell_width, y)

        left_wall = Line(top_left, bottom_left)
        right_wall = Line(top_right, bottom_right)
        top_wall = Line(top_left, top_right)
        bottom_wall = Line(bottom_left, bottom_right)

        canvas = self._win.canvas
        left_wall.draw(
            canvas,
            (ColorType.WALL if self._has_left_wall else ColorType.BACKGROUND),
        )

        right_wall.draw(
            canvas,
            (ColorType.WALL if self._has_right_wall else ColorType.BACKGROUND),
        )

        top_wall.draw(
            canvas,
            (ColorType.WALL if self._has_top_wall else ColorType.BACKGROUND),
        )

        bottom_wall.draw(
            canvas,
            (ColorType.WALL if self._has_bottom_wall else ColorType.BACKGROUND),
        )

    def draw_move(
        self,
        other,
        origin: Point,
        destination: Point,
        cell_width,
        cell_height,
        undo=False,
    ):
        if not self._win:
            return
        path = Line(
            self.get_center(origin, cell_width, cell_height),
            other.get_center(destination, cell_width, cell_height),
        )
        color = ColorType.PATH if undo else ColorType.UNDO
        path.draw(self._win.canvas, color)

    def get_center(self, p: Point, cell_width, cell_height) -> Point:
        return Point(p.x + (cell_width / 2), p.y + (cell_height / 2))

from tkinter import Tk, font, Canvas
from line import Line
from enum import StrEnum
from point import Point


class ColorType(StrEnum):
    BACKGROUND = "white"
    WALL = "black"
    PATH = "grey"
    UNDO = "red"
    PASS = "green"


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.wm_title("Python Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.width = width
        self.height = height
        self.canvas = Canvas(
            self.__root,
            width=width,
            height=height,
            background=ColorType.BACKGROUND,
        )
        self.canvas.pack()
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def clear(self):
        self.canvas.create_rectangle(
            0, 0, self.width, self.height, fill=ColorType.BACKGROUND
        )

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line: Line, fill_color: ColorType):
        line.draw(self.canvas, fill_color)

    def draw_text(self, point: Point, text: str, fill_color: ColorType):
        assert isinstance(self.canvas, Canvas)
        self.canvas.create_text(
            point.x,
            point.y,
            text=text,
            fill=fill_color,
            anchor="center",
            font=("NotoSansM NFM", 20),
        )

    def center(self) -> Point:
        return Point((self.width / 2), (self.height / 2))

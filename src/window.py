from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.wm_title("Python Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack()
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line:Line, fill_color:str):
        line.draw(self.canvas, fill_color)

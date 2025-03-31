from point import Point
import tkinter as tk

class Line:
    def __init__(self, point_a:Point, point_b:Point):
        assert isinstance(point_a,Point)
        assert isinstance(point_b,Point)
        self.a = point_a
        self.b = point_b

    def draw(self, canvas:tk.Canvas, fill_color):
        assert isinstance(canvas, tk.Canvas)

        x1 = self.a.x
        x2 = self.b.x
        y1 = self.a.y
        y2 = self.b.y

        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

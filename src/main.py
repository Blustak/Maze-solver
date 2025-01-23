from window import Window
from line import Line
from point import Point

def main():
    win = Window(800,600)
    points = (
        (Point(0,0), Point(50,50)),
        (Point(0,0), Point(100,50)),
        (Point(50,50), Point(90,72))
    )
    colors = ["red", "green", "blue", "black"]
    lines = [Line(x[0], x[1]) for x in points]
    for (line, color) in zip(lines, colors):
        win.draw_line(line, color)
    win.wait_for_close()

if __name__ == "__main__":
    main()

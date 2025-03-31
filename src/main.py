from window import Window
from cell import Cell
from point import Point

def main():
    win = Window(800, 600)
    a = Cell(Point(10, 10),50,50,win)
    b = Cell(Point(500, 40),30,50,win)
    a.draw()
    b.draw()
    a.draw_move(b, False)
    win.wait_for_close()

if __name__ == "__main__":
    main()

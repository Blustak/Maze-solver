from window import Window
from cell import Cell
def main():
    win = Window(800,600)
    cells = [
        Cell(0,0, win, True, True, True, True),
        Cell(1,1, win, False,False,False,True),
        Cell(5,0,win, True,True,True,True),
    ]
    for cell in cells:
        cell.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()

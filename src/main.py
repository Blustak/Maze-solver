from window import Window
from maze import Maze

def main():
    win = Window(800,600)
    _ = Maze(10,10,5,5,50,50,win)
    win.wait_for_close()

if __name__ == "__main__":
    main()

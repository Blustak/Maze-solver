from window import Window
from maze import Maze

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAZE_WIDTH = 10
MAZE_HEIGHT = 10
CELL_WIDTH = 20
CELL_HEIGHT = 20
MAZE_ORIGIN_X = (SCREEN_WIDTH - (MAZE_WIDTH * CELL_WIDTH)) // 2
MAZE_ORIGIN_Y = (SCREEN_HEIGHT - (MAZE_HEIGHT * CELL_HEIGHT)) // 2


def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    maze = Maze(
        MAZE_ORIGIN_X,
        MAZE_ORIGIN_Y,
        MAZE_WIDTH,
        MAZE_HEIGHT,
        CELL_WIDTH,
        CELL_HEIGHT,
        win,
    )
    solved = maze.solve()
    print("Maze was solved!" if solved else "Maze was not solved...")
    win.wait_for_close()


if __name__ == "__main__":
    main()

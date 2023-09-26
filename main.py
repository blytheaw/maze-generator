from graphics import Window
from maze import Maze
import time

def main():
    win = Window(800, 600)

    maze = Maze(10, 10, 10, 10, 25, 25, win)
    maze.solve()

    win.wait_for_close()

main()

from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 10, 10, 25, 25, win)
    win.wait_for_close()

main()

# Maze Generator

This project randomly generates a graphical maze and then solves it.

Technologies used:

- Python
- Tkinter Python module for GUI

## Setup

- Install Python 3.10 or greater
- Make sure you have required dependencies for the [Tkinter](https://tkdocs.com/tutorial/install.html) Python module

## Run Application

Run `python main.py`

This will execute the maze generator and immediately execute the solving algorithm

## Run Unit Tests

Run `python tests.py`

This will run the test suite. It skips any GUI operations and focuses on maze generation logic.

## Solution

The maze generation uses a recursive BFS traversal of the grid and randomly selects walls to knock down to create the maze.
The primary constraint is that the top left cell is always the start, and the bottom right cell is always the finish.

The maze solving solution uses a recursive DFS traversal to test each direction, starting at the start point.
It checks each direction from the current cell to see if it is the finish cell or if it has a valid path to the finish cell.

## Graphics

Tkinter is used to draw a maze based on dimensions input to the Maze class constructor. It is also used to draw
the paths used when solving the maze. The green path is the solution path, and the red paths are dead ends that were
navigated during solving.

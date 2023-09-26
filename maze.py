from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            rows,
            columns,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._rows = rows
        self._columns = columns
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed != None:
            random.seed(seed)
        else:
            random.seed(0)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, col, row):
        self._animate()
        
        current_cell = self._cells[col][row]
        current_cell.visited = True

        if col == self._columns - 1 and row == self._rows - 1:
            return True

        # up
        if row > 0 and not current_cell.has_top_wall:
            up = self._visit_cell(current_cell, col, row - 1)
            if up == True:
                return True

        # right
        if col < self._columns - 1 and not current_cell.has_right_wall:
            right = self._visit_cell(current_cell, col + 1, row)
            if right == True:
                return True

        # down
        if row < self._rows - 1 and not current_cell.has_bottom_wall:
            down = self._visit_cell(current_cell, col, row + 1)
            if down == True:
                return True

        # left
        if col > 0 and not current_cell.has_left_wall:
            left = self._visit_cell(current_cell, col - 1, row)
            if left == True:
                return True

        return False

    def _visit_cell(self, current, next_col, next_row):
        cell = self._cells[next_col][next_row]
        if not cell.visited:
            current.draw_move(cell)
            next_result = self._solve_r(next_col, next_row)

            if next_result == True:
                return True
            else:
                current.draw_move(cell, undo=True)
                return False

    def _create_cells(self):
        for c in range(self._columns):
            cols = []
            for r in range(self._rows):
                cols.append(Cell(self._win))
            self._cells.append(cols)

        for c in range(self._columns):
            for r in range(self._rows):
                self._draw_cell(c, r)

    def _draw_cell(self, col, row):
        if self._win == None:
            return

        x1 = self._x1 + col * self._cell_size_x
        y1 = self._y1 + row * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[col][row].draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._columns - 1][self._rows - 1].has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(self._columns - 1, self._rows - 1)

    def _reset_cells_visited(self):
        for c in range(self._columns):
            for r in range(self._rows):
                self._cells[c][r].visited = False

    def _break_walls_r(self, col, row):
        current_cell = self._cells[col][row]
        current_cell.visited = True

        while True:
            to_visit = []

            if row > 0:
                up = self._cells[col][row - 1]
                if not up.visited:
                    to_visit.append((col, row - 1))

            if col < self._columns - 1:
                right = self._cells[col + 1][row]
                if not right.visited:
                    to_visit.append((col + 1, row))

            if row < self._rows - 1:
                down = self._cells[col][row + 1]
                if not down.visited:
                    to_visit.append((col, row + 1))

            if col > 0:
                left = self._cells[col - 1][row]
                if not left.visited:
                    to_visit.append((col - 1, row))

            if len(to_visit) == 0:
                self._draw_cell(col, row)
                return

            dir = random.randrange(len(to_visit))

            next_col = to_visit[dir][0]
            next_row = to_visit[dir][1]
            next_cell = self._cells[next_col][next_row]

            if next_col == col and next_row < row:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            if next_col > col and next_row == row:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            if next_col == col and next_row > row:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            if next_col < col and next_row == row:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False

            self._break_walls_r(next_col, next_row)

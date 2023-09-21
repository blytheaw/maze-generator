from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            rows,
            columns,
            cell_size_x,
            cell_size_y,
            win=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.rows = rows
        self.columns = columns
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for c in range(0, self.columns):
            self._cells.append([])
            for r in range(0, self.rows):
                self._cells[c].append(Cell(
                        self.x1 + (self.cell_size_x * c),
                        self.y1 + (self.cell_size_y * r),
                        self.x1 + (self.cell_size_x * (c + 1)),
                        self.y1 + (self.cell_size_y * (r + 1)),
                        win=self.win
                    ))

        for c in range(0, self.columns):
            for r in range(0, self.rows):
                self._draw_cell(self._cells[c][r])

    def _draw_cell(self, cell):
        if self.win == None:
            return

        cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left = self._cells[0][0]
        top_left.has_top_wall = False
        bottom_right = self._cells[self.columns - 1][self.rows - 1]
        bottom_right.has_bottom_wall = False

        self._draw_cell(top_left)
        self._draw_cell(bottom_right)


from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "black")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "white")
        
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "black")
        else:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "white")

        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "black")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "white")

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "black")
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "white")

    def draw_move(self, to_cell, undo=False):
        fill_color = "green"
        if undo:
            fill_color = "red"

        current_center_x = self.get_center_x()
        current_center_y = self.get_center_y()
        to_center_x = to_cell.get_center_x()
        to_center_y = to_cell.get_center_y()

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, current_center_y), Point(current_center_x, current_center_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_center_x, to_center_y), Point(to_cell._x2, to_center_y))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(current_center_x, current_center_y), Point(self._x2, current_center_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_center_y), Point(to_center_x, to_center_y))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(current_center_x, current_center_y), Point(current_center_x, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_center_x, to_cell._y2), Point(to_center_x, to_center_y))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(current_center_x, current_center_y), Point(current_center_x, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_center_x, to_center_y), Point(to_center_x, to_cell._y1))
            self._win.draw_line(line, fill_color)

    def get_center_x(self):
        return (self._x1 + self._x2) / 2

    def get_center_y(self):
        return (self._y1 + self._y2) / 2

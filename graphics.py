import random
from tkinter import Tk, BOTH, Canvas
import time

class Point():
    """
    A class to represent a point in 2D space.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    """
    A class to represent a line segment between two points.
    Attributes:
    ----------
    p1 : Point
        The starting point of the line.
    p2 : Point
        The ending point of the line.
    Methods:
    -------
    draw(canvas, fill_color):
        Draws the line on the given canvas with the specified fill color.
    """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Window():
    """
    A class to represent a graphical window for the Maze Solver application.
    Attributes
    ----------
    __root_widget : Tk
        The main Tkinter window widget.
    __canvas : Canvas
        The canvas widget where graphics are drawn.
    __window_running : bool
        A flag to indicate if the window is currently running.
    Methods
    -------
    redraw():
        Updates the window by processing any pending events.
    wait_for_close():
        Keeps the window open and processes events until the window is closed.
    close():
        Closes the window and stops the event loop.
    draw_line(line, fill_color="black"):
        Draws a line on the canvas with the specified fill color.
    """
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title = "Maze Solver"
        self.__canvas = Canvas(height=height, width=width)
        self.__canvas.pack()
        self.__window_running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()
    
    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
    
    def close(self):
        print("Closing...")
        self.__window_running = False
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

class Cell():
    """
    Represents a cell in a maze with walls and a visited state.
    Attributes:
        has_left_wall (bool): Indicates if the cell has a left wall.
        has_right_wall (bool): Indicates if the cell has a right wall.
        has_top_wall (bool): Indicates if the cell has a top wall.
        has_bottom_wall (bool): Indicates if the cell has a bottom wall.
        visited (bool): Indicates if the cell has been visited.
        _x1 (int): The x-coordinate of the top-left corner of the cell.
        _y1 (int): The y-coordinate of the top-left corner of the cell.
        _x2 (int): The x-coordinate of the bottom-right corner of the cell.
        _y2 (int): The y-coordinate of the bottom-right corner of the cell.
        _window (object): The window object where the cell is drawn.
    Methods:
        __init__(window):
            Initializes a new cell with walls and a visited state.
        draw(x1, y1, x2, y2):
            Draws the cell on the window with the specified coordinates.
        draw_move(to_cell, undo=False):
            Draws a move from the current cell to another cell.
    """
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._window = window
    
    def draw(self, x1, y1, x2, y2):
        if self._window is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(line, "#d9d9d9")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(line, "#d9d9d9")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(line, "#d9d9d9")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(line, "#d9d9d9")
    
    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
            
        self._window.draw_line(Line(Point((self._x1+self._x2)//2, (self._y1+self._y2)//2), Point((to_cell._x1+to_cell._x2)//2, (to_cell._y1+to_cell._y2)//2)), fill_color)

class Grid():
    """
    A class to represent a grid for maze generation and solving.
    Attributes
    ----------
    _cells : list
        A 2D list to store the cells of the grid.
    _x1 : int
        The x-coordinate of the top-left corner of the grid.
    _y1 : int
        The y-coordinate of the top-left corner of the grid.
    _num_rows : int
        The number of rows in the grid.
    _num_cols : int
        The number of columns in the grid.
    _cell_size_x : int
        The width of each cell in the grid.
    _cell_size_y : int
        The height of each cell in the grid.
    _window : object, optional
        The window object for drawing the grid (default is None).
    Methods
    -------
    _create_cells():
        Creates the cells of the grid.
    _draw_cell(i, j):
        Draws a cell at the specified position.
    _animate():
        Redraws the window and pauses for a short duration.
    _break_entrance_and_exit():
        Breaks the walls for the entrance and exit of the maze.
    _break_walls_r(i, j):
        Recursively breaks walls to generate the maze.
    _reset_cells_visited():
        Resets the visited status of all cells.
    _solve_r(i, j):
        Recursively solves the maze using depth-first search.
    solve():
        Initiates the maze solving process.
    """
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._window))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._window is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.02)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    # returns True if this is the end cell, OR if it leads to the end cell.
    # returns False if this is a loser cell.
    def _solve_r(self, i, j):
        self._animate()

        # vist the current cell
        self._cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False

    # create the moves for the solution using a depth first search
    def solve(self):
        return self._solve_r(0, 0)
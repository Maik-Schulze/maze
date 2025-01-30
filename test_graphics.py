import unittest
from graphics import *

class TestGrid(unittest.TestCase):
    def test_grid_initialization(self):
        window = Window(400, 400)
        grid = Grid(0, 0, 10, 10, 40, 40, window)
        self.assertEqual(len(grid._cells), 10)
        self.assertEqual(len(grid._cells[0]), 10)
        window.close()
    
    def test_draw_cell(self):
        window = Window(400, 400)
        grid = Grid(0, 0, 10, 10, 40, 40, window)
        cell = grid._cells[0][0]
        cell.draw(0, 0, 40, 40)
        self.assertEqual(cell._x1, 0)
        self.assertEqual(cell._y1, 0)
        self.assertEqual(cell._x2, 40)
        self.assertEqual(cell._y2, 40)
        window.close()
    
    def test_draw_move(self):
        window = Window(400, 400)
        grid = Grid(0, 0, 10, 10, 40, 40, window)
        cell1 = grid._cells[0][0]
        cell2 = grid._cells[0][1]
        cell1.draw(0, 0, 40, 40)
        cell2.draw(40, 0, 80, 40)
        cell1.draw_move(cell2)
        self.assertEqual(cell1._x2, 40)
        self.assertEqual(cell2._x1, 40)
        window.close()
    
    def test_reset_cells_visited(self):
        window = Window(400, 400)
        grid = Grid(0, 0, 10, 10, 40, 40, window)
        for col in grid._cells:
            for cell in col:
                cell.visited = True
        grid._reset_cells_visited()
        for col in grid._cells:
            for cell in col:
                self.assertFalse(cell.visited)
        window.close()

class TestPoint(unittest.TestCase):
    def test_point_initialization(self):
        point = Point(5, 10)
        self.assertEqual(point.x, 5)
        self.assertEqual(point.y, 10)

class TestLine(unittest.TestCase):
    def test_line_initialization(self):
        p1 = Point(0, 0)
        p2 = Point(10, 10)
        line = Line(p1, p2)
        self.assertEqual(line.p1, p1)
        self.assertEqual(line.p2, p2)

    def test_line_draw(self):
        p1 = Point(0, 0)
        p2 = Point(10, 10)
        line = Line(p1, p2)
        window = Window(400, 400)
        canvas = window._Window__canvas
        line.draw(canvas, "black")
        # Since we can't directly test the canvas, we assume no exceptions mean success
        window.close()

class TestWindow(unittest.TestCase):
    def test_window_initialization(self):
        window = Window(400, 400)
        self.assertIsInstance(window, Window)
        window.close()

    def test_window_redraw(self):
        window = Window(400, 400)
        try:
            window.redraw()
        except Exception as e:
            self.fail(f"redraw() raised {e} unexpectedly!")
        window.close()

    def test_window_draw_line(self):
        window = Window(400, 400)
        p1 = Point(0, 0)
        p2 = Point(10, 10)
        line = Line(p1, p2)
        try:
            window.draw_line(line)
        except Exception as e:
            self.fail(f"draw_line() raised {e} unexpectedly!")
        window.close()

class TestCell(unittest.TestCase):
    def test_cell_initialization(self):
        window = Window(400, 400)
        cell = Cell(window)
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)
        window.close()

    def test_cell_draw(self):
        window = Window(400, 400)
        cell = Cell(window)
        cell.draw(0, 0, 40, 40)
        self.assertEqual(cell._x1, 0)
        self.assertEqual(cell._y1, 0)
        self.assertEqual(cell._x2, 40)
        self.assertEqual(cell._y2, 40)
        window.close()

    def test_cell_draw_move(self):
        window = Window(400, 400)
        cell1 = Cell(window)
        cell2 = Cell(window)
        cell1.draw(0, 0, 40, 40)
        cell2.draw(40, 0, 80, 40)
        cell1.draw_move(cell2)
        self.assertEqual(cell1._x2, 40)
        self.assertEqual(cell2._x1, 40)
        window.close()


if __name__ == "__main__":
    unittest.main()
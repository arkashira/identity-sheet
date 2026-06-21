from identity_sheet import Grid, Cell
import pytest

def test_render_grid():
    grid = Grid(2, 2, [[Cell("1"), Cell("2")], [Cell("3"), Cell("4")]])
    # Capture stdout
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    grid.render()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "Cell (0, 0): 1\nCell (0, 1): 2\nCell (1, 0): 3\nCell (1, 1): 4\n"

def test_edit_cell():
    grid = Grid(2, 2, [[Cell("1"), Cell("2")], [Cell("3"), Cell("4")]])
    grid.edit_cell(0, 0, "5")
    assert grid.cells[0][0].value == "5"

def test_recalculate():
    grid = Grid(2, 2, [[Cell("1"), Cell("2")], [Cell("3"), Cell("4")]])
    grid.cells[0][0].formula = "1 + 1"
    grid.recalculate()
    assert grid.cells[0][0].value == "2"

def test_display_error_messages():
    grid = Grid(2, 2, [[Cell("1"), Cell("2")], [Cell("3"), Cell("4")]])
    grid.cells[0][0].formula = "1 / 0"
    grid.recalculate()
    # Capture stdout
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    grid.display_error_messages()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "Error in cell (0, 0): Error: division by zero\n"

def test_invalid_formula():
    grid = Grid(2, 2, [[Cell("1"), Cell("2")], [Cell("3"), Cell("4")]])
    grid.cells[0][0].formula = "invalid formula"
    grid.recalculate()
    assert "Error:" in grid.cells[0][0].value

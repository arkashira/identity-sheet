from dataclasses import dataclass
from typing import List

@dataclass
class Cell:
    value: str
    formula: str = ""

@dataclass
class Grid:
    rows: int
    cols: int
    cells: List[List[Cell]]

    def render(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                print(f"Cell ({row}, {col}): {cell.value}")

    def edit_cell(self, row: int, col: int, new_value: str):
        self.cells[row][col].value = new_value
        self.recalculate()

    def recalculate(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                if cell.formula:
                    try:
                        cell.value = str(eval(cell.formula))
                    except Exception as e:
                        cell.value = f"Error: {str(e)}"

    def display_error_messages(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.cells[row][col]
                if "Error:" in cell.value:
                    print(f"Error in cell ({row}, {col}): {cell.value}")

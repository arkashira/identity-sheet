from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Cell:
    value: str
    dependent_calculations: List[str]

class IdentitySheet:
    def __init__(self):
        self.cells: Dict[str, Cell] = {}

    def add_cell(self, cell_id: str, value: str, dependent_calculations: List[str]):
        self.cells[cell_id] = Cell(value, dependent_calculations)

    def get_dependent_calculations(self, cell_id: str) -> List[str]:
        return self.cells.get(cell_id, Cell("", [])).dependent_calculations

    def move_cell(self, cell_id: str, new_position: str) -> Dict[str, str]:
        affected_calculations = []
        for cell in self.cells.values():
            if cell_id in cell.dependent_calculations:
                affected_calculations.append(cell.value)
        self.cells[new_position] = self.cells.pop(cell_id)
        return {"affected_calculations": affected_calculations, "new_position": new_position}

    def highlight_affected_calculations(self, cell_id: str) -> List[str]:
        affected_calculations = []
        for cell in self.cells.values():
            if cell_id in cell.dependent_calculations:
                affected_calculations.append(cell.value)
        return affected_calculations

    def summarize_impact(self, cell_id: str) -> str:
        dependent_calculations = self.get_dependent_calculations(cell_id)
        affected_calculations = self.highlight_affected_calculations(cell_id)
        return f"Moving cell {cell_id} affects {len(affected_calculations)} calculations: {', '.join(affected_calculations)}"

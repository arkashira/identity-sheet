from identity_sheet import IdentitySheet, Cell
import pytest

def test_add_cell():
    sheet = IdentitySheet()
    sheet.add_cell("A1", "10", ["B1", "C1"])
    assert sheet.get_dependent_calculations("A1") == ["B1", "C1"]

def test_get_dependent_calculations():
    sheet = IdentitySheet()
    sheet.add_cell("A1", "10", ["B1", "C1"])
    assert sheet.get_dependent_calculations("A1") == ["B1", "C1"]
    assert sheet.get_dependent_calculations("A2") == []

def test_move_cell():
    sheet = IdentitySheet()
    sheet.add_cell("A1", "10", ["B1", "C1"])
    sheet.add_cell("B1", "20", ["A1"])
    result = sheet.move_cell("A1", "A2")
    assert result["affected_calculations"] == ["20"]
    assert result["new_position"] == "A2"

def test_highlight_affected_calculations():
    sheet = IdentitySheet()
    sheet.add_cell("A1", "10", ["B1", "C1"])
    sheet.add_cell("B1", "20", ["A1"])
    assert sheet.highlight_affected_calculations("A1") == ["20"]

def test_summarize_impact():
    sheet = IdentitySheet()
    sheet.add_cell("A1", "10", ["B1", "C1"])
    sheet.add_cell("B1", "20", ["A1"])
    assert sheet.summarize_impact("A1") == "Moving cell A1 affects 1 calculations: 20"

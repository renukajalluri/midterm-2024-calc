import pytest
from calculator.calculator import Calculator
from calculator.history import HistoryFacade
import os

# Helper function to reset the history file for test isolation
def reset_history_file():
    history_file = "calculation_history.csv"
    if os.path.exists(history_file):
        os.remove(history_file)

# Fixture to create a fresh instance of Calculator for each test
@pytest.fixture
def calc():
    reset_history_file()  # Ensure no pre-existing history
    return Calculator()

@pytest.fixture
def history_facade():
    reset_history_file()
    return HistoryFacade()

### Tests for the Calculator class ###

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert "Added 2 + 3 = 5" in calc.show_history()

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(-3, -2) == -1
    assert "Subtracted 5 - 3 = 2" in calc.show_history()

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 10) == 0
    assert "Multiplied 3 * 4 = 12" in calc.show_history()

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(-10, 5) == -2
    assert "Divided 10 / 2 = 5.0" in calc.show_history()

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(10, 0)

def test_show_history(calc):
    calc.add(1, 2)
    calc.multiply(3, 4)
    history = calc.show_history()
    assert "Added 1 + 2 = 3" in history
    assert "Multiplied 3 * 4 = 12" in history

def test_clear_history(calc):
    calc.add(1, 1)
    calc.clear_history()
    assert calc.show_history() == "No history available."

def test_delete_history_record(calc):
    calc.add(1, 1)
    calc.add(2, 2)
    assert calc.delete_history_record(1) == "Deleted record: Added 2 + 2 = 4"
    assert "Added 2 + 2 = 4" not in calc.show_history()

def test_delete_invalid_index(calc):
    calc.add(1, 1)
    assert calc.delete_history_record(5) == "Invalid index. No record deleted."

def test_save_and_load_history(calc):
    calc.add(5, 5)
    calc.save_history()
    assert os.path.exists("calculation_history.csv")

    # Create a new instance to test loading
    new_calc = Calculator()
    loaded_history = new_calc.load_history()
    assert "Added 5 + 5 = 10" in loaded_history

### Tests for the HistoryFacade class ###

def test_add_entry(history_facade):
    history_facade.add_entry("Test Entry")
    assert "Test Entry" in history_facade.show_history()

def test_save_history(history_facade):
    history_facade.add_entry("Entry to Save")
    history_facade.save_history()
    assert os.path.exists("calculation_history.csv")

def test_load_history(history_facade):
    history_facade.add_entry("Entry to Load")
    history_facade.save_history()

    new_facade = HistoryFacade()
    assert "Entry to Load" in new_facade.show_history()

def test_clear_history(history_facade):
    history_facade.add_entry("Clear This Entry")
    history_facade.clear_history()
    assert history_facade.show_history() == "No history available."

def test_delete_entry(history_facade):
    history_facade.add_entry("Delete Me")
    assert history_facade.delete_entry(0) == "Deleted record: Delete Me"
    assert history_facade.show_history() == "No history available."

def test_delete_invalid_entry(history_facade):
    assert history_facade.delete_entry(5) == "Invalid index. No record deleted."

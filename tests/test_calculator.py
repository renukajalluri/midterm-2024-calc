"""
Module for testing the Calculator and HistoryFacade classes.

This module contains pytest fixtures for setting up test environments 
and various test cases to validate the functionality of the Calculator 
and HistoryFacade classes, ensuring operations like addition, subtraction, 
history management, and persistence are working as expected.
"""
import os  # Standard library imports
import pytest  # Third-party imports
from calculator.calculator import Calculator  # Local application imports
from calculator.history import HistoryFacade  # Local application imports


# Helper function to reset the history file for test isolation
def reset_history_file():
    """Remove the history file if it exists to ensure test isolation."""
    history_file = "calculation_history.csv"
    if os.path.exists(history_file):
        os.remove(history_file)

# Fixture to create a fresh instance of Calculator for each test
@pytest.fixture
def calc_fixture():
    """Provide a fresh instance of Calculator with a reset history file."""
    reset_history_file()  # Ensure no pre-existing history
    return Calculator()
@pytest.fixture
def history_facade_fixture():
    """Provide a fresh instance of HistoryFacade with a reset history file."""
    reset_history_file()
    return HistoryFacade()

### Tests for the Calculator class ###

def test_add(calc_fixture):
    """Test the addition functionality of the Calculator."""
    assert calc_fixture.add(2, 3) == 5
    assert calc_fixture.add(-1, 1) == 0
    assert "Added 2 + 3 = 5" in calc_fixture.show_history()

def test_subtract(calc_fixture):
    """Test the subtraction functionality of the Calculator."""
    assert calc_fixture.subtract(5, 3) == 2
    assert calc_fixture.subtract(-3, -2) == -1
    assert "Subtracted 5 - 3 = 2" in calc_fixture.show_history()

def test_multiply(calc_fixture):
    """Test the multiplication functionality of the Calculator."""
    assert calc_fixture.multiply(3, 4) == 12
    assert calc_fixture.multiply(0, 10) == 0
    assert "Multiplied 3 * 4 = 12" in calc_fixture.show_history()

def test_divide(calc_fixture):
    """Test the division functionality of the Calculator."""
    assert calc_fixture.divide(10, 2) == 5
    assert calc_fixture.divide(-10, 5) == -2
    assert "Divided 10 / 2 = 5.0" in calc_fixture.show_history()

def test_divide_by_zero(calc_fixture):
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc_fixture.divide(10, 0)

def test_show_history(calc_fixture):
    """Test the history display functionality of the Calculator."""
    calc_fixture.add(1, 2)
    calc_fixture.multiply(3, 4)
    history = calc_fixture.show_history()
    assert "Added 1 + 2 = 3" in history
    assert "Multiplied 3 * 4 = 12" in history

def test_clear_history(calc_fixture):
    """Test clearing the history in the Calculator."""
    calc_fixture.add(1, 1)
    calc_fixture.clear_history()
    assert calc_fixture.show_history() == "No history available."

def test_delete_history_record(calc_fixture):
    """Test deleting a specific history record in the Calculator."""
    calc_fixture.add(1, 1)
    calc_fixture.add(2, 2)
    assert calc_fixture.delete_history_record(1) == "Deleted record: Added 2 + 2 = 4"
    assert "Added 2 + 2 = 4" not in calc_fixture.show_history()

def test_delete_invalid_index(calc_fixture):
    """Test attempting to delete an invalid history record index."""
    calc_fixture.add(1, 1)
    assert calc_fixture.delete_history_record(5) == "Invalid index. No record deleted."

def test_save_and_load_history(calc_fixture):
    """Test saving and loading the calculation history."""
    calc_fixture.add(5, 5)
    calc_fixture.save_history()
    assert os.path.exists("calculation_history.csv")

    # Create a new instance to test loading
    new_calc = Calculator()
    loaded_history = new_calc.load_history()
    assert "Added 5 + 5 = 10" in loaded_history

### Tests for the HistoryFacade class ###

def test_add_entry(history_facade_fixture ):
    """Test adding an entry to the history via HistoryFacade."""
    history_facade_fixture .add_entry("Test Entry")
    assert "Test Entry" in history_facade_fixture .show_history()

def test_save_history(history_facade_fixture ):
    """Test saving the history via HistoryFacade."""
    history_facade_fixture .add_entry("Entry to Save")
    history_facade_fixture .save_history()
    assert os.path.exists("calculation_history.csv")

def test_load_history(history_facade_fixture ):
    """Test loading history entries via HistoryFacade."""
    history_facade_fixture .add_entry("Entry to Load")
    history_facade_fixture .save_history()

    new_facade = HistoryFacade()
    assert "Entry to Load" in new_facade.show_history()

def test_clear_history_facade(history_facade_fixture ):
    """Test clearing the history via HistoryFacade."""
    history_facade_fixture .add_entry("Clear This Entry")
    history_facade_fixture .clear_history()
    assert history_facade_fixture .show_history() == "No history available."


def test_delete_entry(history_facade_fixture ):
    """Test deleting an entry in the history via HistoryFacade."""
    history_facade_fixture .add_entry("Delete Me")
    assert history_facade_fixture.delete_entry(0) == "Deleted record: Delete Me"
    assert history_facade_fixture.show_history() == "No history available."

def test_delete_invalid_entry(history_facade_fixture):
    """Test attempting to delete a non-existent entry in the history."""
    assert history_facade_fixture.delete_entry(5) == "Invalid index. No record deleted."

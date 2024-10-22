import logging
from calculator.history import HistoryFacade


class Calculator:
    """The main calculator class that performs basic arithmetic operations and manages plugins."""    
    def __init__(self):
        self.history_facade = HistoryFacade()
    def add(self, a, b):
        """Return the sum of a and b."""
        result = a + b
        entry = f"Added {a} + {b} = {result}"
        self.history_facade.add_entry(entry)
        logging.info(entry)
        return result

    def subtract(self, a, b):
        """Return the result of a minus b."""
        result = a - b
        entry = f"Subtracted {a} - {b} = {result}"
        self.history_facade.add_entry(entry)
        logging.info(entry)
        return result

    def multiply(self, a, b):
        """Return the product of a and b."""
        result = a * b
        entry = f"Multiplied {a} * {b} = {result}"
        self.history_facade.add_entry(entry)
        logging.info(entry)
        return result

    def divide(self, a, b):
        """Return the result of a divided by b."""
        if b == 0:
            logging.error("Division by zero attempted.")
            raise ValueError("Cannot divide by zero.")
        result = a / b
        entry = f"Divided {a} / {b} = {result}"
        self.history_facade.add_entry(entry)
        logging.info(entry)
        return result

    def show_history(self):
        """Show the current calculation history."""
        return self.history_facade.show_history()

    def save_history(self):
        """Save the current history to a CSV file."""
        self.history_facade.save_history()
        return "History saved."

    def load_history(self):
        """Load history from a CSV file and return it as a string."""
        loaded_history = self.history_facade.load_history()
        if not loaded_history.empty:
            return loaded_history.to_string(index=False)
        return "No history found."

    def clear_history(self):
        """Clear the current calculation history."""
        self.history_facade.clear_history()
        return "History cleared."

    def delete_history_record(self, index):
        """Delete a specific record from the history."""
        return self.history_facade.delete_entry(index)

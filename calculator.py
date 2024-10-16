# File: calculator.py

import pandas as pd
import os
from plugin import Plugin

class Calculator:
    """The main calculator class that performs basic arithmetic operations and manages plugins."""
    
    def __init__(self):
        self.history = []
        self.plugins = {}
        self.history_file = "calculation_history.csv"  # CSV file for history

    def add(self, a, b):
        result = a + b
        self.history.append(f"Added {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"Subtracted {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"Multiplied {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"Divided {a} / {b} = {result}")
        return result

    def show_history(self):
        """Show the current calculation history."""
        return "\n".join(self.history) if self.history else "No history available."

    def save_history(self):
        """Save the current history to a CSV file."""
        df = pd.DataFrame(self.history, columns=["Calculation"])
        df.to_csv(self.history_file, index=False)
        return f"History saved to '{self.history_file}'."

    def load_history(self):
        """Load history from a CSV file and return it as a string."""
        if os.path.exists(self.history_file):
            df = pd.read_csv(self.history_file)
            self.history = df['Calculation'].tolist()
            loaded_history = "\n".join(self.history) if self.history else "No history found in file."
            return f"History loaded from '{self.history_file}':\n{loaded_history}"
        else:
            return "No history file found."

    def clear_history(self):
        """Clear the current calculation history."""
        self.history = []
        return "History cleared."

    def delete_history_record(self, index):
        """Delete a specific record from the history."""
        if 0 <= index < len(self.history):
            deleted_record = self.history.pop(index)
            return f"Deleted record: {deleted_record}"
        else:
            return "Invalid index. No record deleted."

    def register_plugin(self, plugin):
        """Register a new plugin and its commands."""
        if isinstance(plugin, Plugin):
            self.plugins[plugin.__class__.__name__.lower()] = plugin
            print(f"Plugin '{plugin.__class__.__name__}' registered successfully.")

    def list_plugins(self):
        """List all available plugin commands."""
        return self.plugins

import pandas as pd
import os
import logging

class HistoryFacade:
    """Facade class for managing history using Pandas DataFrame."""
    
    def __init__(self, history_file="calculation_history.csv"):
        self.history_file = history_file
        self.history_df = pd.DataFrame(columns=["Calculation"])  # Initialize an empty DataFrame
        if os.path.exists(self.history_file):
            self.history_df = pd.read_csv(self.history_file)
        else:
            self.save_history()  # Create an empty history file if it doesn't exist

    def add_entry(self, entry):
        """Add a new entry to the history DataFrame."""
        new_entry = {"Calculation": entry}
        self.history_df = pd.concat([self.history_df, pd.DataFrame([new_entry])], ignore_index=True)

    def save_history(self):
        """Save the DataFrame to a CSV file."""
        self.history_df.to_csv(self.history_file, index=False)
        logging.info(f"History saved to '{self.history_file}'.")

    def load_history(self):
        """Load the history from a CSV file."""
        if os.path.exists(self.history_file):
            self.history_df = pd.read_csv(self.history_file)
            logging.info(f"History loaded from '{self.history_file}'.")
            return self.history_df
        else:
            logging.warning("No history file found.")
            return pd.DataFrame(columns=["Calculation"])  # Return empty DataFrame if file not found

    def clear_history(self):
        """Clear the history DataFrame."""
        self.history_df = pd.DataFrame(columns=["Calculation"])
        logging.info("History cleared.")

    def delete_entry(self, index):
        """Delete a specific entry by index."""
        if 0 <= index < len(self.history_df):
            deleted_record = self.history_df.iloc[index]
            self.history_df = self.history_df.drop(index).reset_index(drop=True)
            logging.info(f"Deleted record: {deleted_record['Calculation']}")
            return f"Deleted record: {deleted_record['Calculation']}"
        else:
            logging.error("Invalid index provided for deletion.")
            return "Invalid index. No record deleted."

    def show_history(self):
        """Return a string representation of the current history."""
        if not self.history_df.empty:
            return self.history_df.to_string(index=False)
        else:
            return "No history available."

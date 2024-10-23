"""
DataPlugin module.

This module defines the DataPlugin class, which is a plugin for the 
Command framework. It provides functionality to read and display 
data from a specified CSV file.
"""
import logging
import csv
import os
from commands import Command

class DataPlugin(Command):
    """A plugin that displays data from a CSV file."""
    command_name = "data"

    @staticmethod
    def execute():
        """Execute the data command to display contents of a CSV file."""
        # filename = "data/books.csv"  # Specify the filename here
        filename = os.getenv("books_file_path")
        try:
            with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)  # Get the headers
                print(f"{' | '.join(headers)}")  # Print headers

                # Print the rows
                for row in reader:
                    print(f"{' | '.join(row)}")                
                logging.info("Displayed data from CSV file: %s", filename)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
            logging.error("File not found: %s", filename)
        except Exception as e:
            print("Error reading the CSV file:", e)
            logging.error("Error reading CSV file %s: %s", filename, e)
# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ
import pytest
import logging
import os

from plugins.data import DataPlugin

# Test case for successfully reading the CSV file
def test_data_plugin_execute_success(monkeypatch, capfd, caplog, tmpdir):
    """Test the execute method when the CSV file exists and is readable."""
    
    # Create a temporary CSV file with sample content
    test_csv = tmpdir.join("books.csv")
    test_csv.write("Title,Author\nThe Great Gatsby,F. Scott Fitzgerald\n1984,George Orwell")

    # Set the environment variable to point to the temp CSV file
    monkeypatch.setenv("books_file_path", str(test_csv))

    # Capture the log output
    with caplog.at_level(logging.INFO):
        # Execute the data command
        DataPlugin.execute()

        # Capture the printed output
        out, err = capfd.readouterr()

        # Verify the printed output (headers and rows)
        assert "Title | Author" in out
        assert "The Great Gatsby | F. Scott Fitzgerald" in out
        assert "1984 | George Orwell" in out

        # Verify the log output
        assert f"Displayed data from CSV file: {test_csv}" in caplog.text


# Test case for FileNotFoundError
def test_data_plugin_execute_file_not_found(monkeypatch, capfd, caplog):
    """Test the execute method when the CSV file does not exist."""
    
    # Set an invalid path for the environment variable
    monkeypatch.setenv("books_file_path", "invalid/path/to/books.csv")

    # Capture the log output
    with caplog.at_level(logging.ERROR):
        # Execute the data command
        DataPlugin.execute()

        # Capture the printed output
        out, err = capfd.readouterr()

        # Verify the error message is printed
        assert "Error: The file 'invalid/path/to/books.csv' was not found." in out

        # Verify the log output
        assert "File not found: invalid/path/to/books.csv" in caplog.text


# Test case for generic Exception
def test_data_plugin_execute_exception(monkeypatch, capfd, caplog):
    """Test the execute method when an unexpected exception occurs."""
    
    # Set the environment variable to a directory instead of a file to trigger an exception
    monkeypatch.setenv("books_file_path", "/")

    # Capture the log output
    with caplog.at_level(logging.ERROR):
        # Execute the data command
        DataPlugin.execute()

        # Capture the printed output
        out, err = capfd.readouterr()

        # Verify the generic error message is printed
        assert "Error reading the CSV file:" in out

        # Verify the log output
        assert "Error reading CSV file /" in caplog.text

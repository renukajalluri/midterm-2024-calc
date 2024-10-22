"""
TimePlugin module.

This module defines the TimePlugin class, which is a plugin for the 
Command framework. It provides functionality to display the current time.
"""
import logging
from commands import Command
from datetime import datetime

class TimePlugin(Command):
    """A plugin that displays the current time."""
    command_name = "time"

    @staticmethod
    def execute():
        """Execute the time command to display the current time."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Current Time:", current_time)
        logging.info("Displayed current time: %s", current_time)

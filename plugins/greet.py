"""
GreetPlugin module.

This module defines the GreetPlugin class, which is a plugin for the 
Command framework. It provides functionality to greet users by 
printing specified arguments along with a greeting message.
"""

from commands import Command

class GreetPlugin(Command):
    """An example plugin that provides additional functionality."""

    command_name = "greet"

    @staticmethod
    def execute(arg1, arg2):
        """Execute the greet command with two arguments."""
        print(arg1, arg2)
        print("greet")

# pylint: disable=too-few-public-methods
# pylint: disable=arguments-differ

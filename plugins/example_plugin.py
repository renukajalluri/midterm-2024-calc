# File: plugins/example_plugin.py

from plugin import Plugin  # Import the Plugin class from the plugin module

class ExamplePlugin(Plugin):
    """An example plugin that provides additional functionality."""
    def execute(self, operation, num1, num2):
        """Execute a simple operation."""
        if operation == "add":
            return f"Plugin Result: {num1} + {num2} = {num1 + num2}"
        elif operation == "subtract":
            return f"Plugin Result: {num1} - {num2} = {num1 - num2}"
        else:
            return "Unknown operation in Example Plugin."

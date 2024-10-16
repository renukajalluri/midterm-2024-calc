
from plugin import Plugin


class Calculator:
    """The main calculator class that performs basic arithmetic operations and manages plugins."""
    def __init__(self):
        self.history = []
        self.plugins = {}

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
        return "\n".join(self.history)

    def register_plugin(self, plugin):
        """Register a new plugin and its commands."""
        if isinstance(plugin, Plugin):
            self.plugins[plugin.__class__.__name__.lower()] = plugin
            print(f"Plugin '{plugin.__class__.__name__}' registered successfully.")

    def list_plugins(self):
        """List all available plugin commands."""
        return self.plugins

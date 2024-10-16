# File: plugin.py

import importlib
import os
import inspect

class Plugin:
    """Base class for all plugins. Each plugin must implement the execute method."""
    def execute(self, *args):
        """Execute the plugin command with given arguments."""
        raise NotImplementedError("Plugin must implement the execute method.")

class PluginManager:
    """Class to manage loading plugins dynamically."""
    def __init__(self, calculator):
        self.calculator = calculator

    def load_plugins(self, plugins_directory):
        """Dynamically load plugins from the specified directory."""
        for filename in os.listdir(plugins_directory):
            if filename.endswith(".py") and not filename.startswith("_"):
                module_name = filename[:-3]
                module = importlib.import_module(f"plugins.{module_name}")

                # Register each class that inherits from Plugin
                for name, cls in inspect.getmembers(module, inspect.isclass):
                    if issubclass(cls, Plugin) and cls is not Plugin:
                        self.calculator.register_plugin(cls())

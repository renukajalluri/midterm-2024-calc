"""
This module provides a framework for dynamically loading and executing plugins.

It defines the `Command` base class that all plugins must inherit from, and the
`CommandHandler` singleton class that manages the registration and execution of
these commands. 

Classes:
- Command: Base class for all plugins.
- CommandHandler: Manages plugin loading and command execution.

Usage:
1. Define a plugin by subclassing `Command`.
2. Implement the `execute` method in the plugin.
3. Use `CommandHandler` to load and execute the plugin commands.
"""
import importlib
import logging
import os
import inspect

class Command:
    """Base class for all plugins. Each plugin must implement the execute method."""
    def execute(self, *args):
        """Execute the plugin command with given arguments."""
        raise NotImplementedError("Plugin must implement the execute method.")

class CommandHandler:
    """Singleton class to manage loading plugins dynamically."""
    _instance = None

    def __new__(cls):
        """Override the __new__ method to ensure only one instance of the class."""
        if cls._instance is None:
            cls._instance = super(CommandHandler, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize instance attributes."""
        if not hasattr(self, 'commands'):
            self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Register a command with a given name.

    Args:
        command_name (str): The name of the command to register.
        command (Command): The command instance to associate with the command name.
    """
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Easier to ask for forgiveness than permission (EAFP) - Use when it's most likely to work."""
        try:
            self.commands[command_name].execute()
        except KeyError:
            logging.error(f"No such command: {command_name}")

    def load_plugins(self, plugins_directory):
        """Dynamically load plugins from the specified directory."""
        for filename in os.listdir(plugins_directory):
            if filename.endswith(".py") and not filename.startswith("_"):
                module_name = filename[:-3]  # removed .py which is of 3 characters
                module = importlib.import_module(f"plugins.{module_name}")
                # Register each class that inherits from Command
                for _, cls in inspect.getmembers(module, inspect.isclass):
                    if issubclass(cls, Command) and cls is not Command:
                        # used to identify the arguments
                        signature = inspect.signature(cls.execute)
                        arguments = signature.parameters.values()                      
                        self.register_plugin(cls.command_name, cls(), list(arguments))

    def register_plugin(self, command_name, plugin, arguments):
        """Register a new plugin and its commands."""
        if isinstance(plugin, Command):
            logging.info("Plugin '%s' registered successfully.", plugin.__class__.__name__)
            if len(arguments) > 1:
                self.commands[command_name] = [plugin, f"No of Arguments is {len(arguments) - 1} & Arguments are {arguments[1:]}"]
            else:
                self.commands[command_name] = [plugin, f"No of Arguments is {len(arguments) - 1}"]

    def list_plugins(self):
        """List all available plugin commands."""
        return list(self.commands.keys())

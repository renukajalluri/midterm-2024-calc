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
            cls._instance.commands = {}
        return cls._instance

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when it's most likely to work."""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

    def load_plugins(self, plugins_directory):
        """Dynamically load plugins from the specified directory."""
        for filename in os.listdir(plugins_directory):
            if filename.endswith(".py") and not filename.startswith("_"):
                module_name = filename[:-3]
                module = importlib.import_module(f"plugins.{module_name}")

                # Register each class that inherits from Command
                for name, cls in inspect.getmembers(module, inspect.isclass):
                    if issubclass(cls, Command) and cls is not Command:
                        signature = inspect.signature(cls.execute)
                        arguments = signature.parameters.values()
                        self.register_plugin(cls(), list(arguments))

    def register_plugin(self, plugin, arguments):
        """Register a new plugin and its commands."""
        if isinstance(plugin, Command):
            logging.info(f"Plugin '{plugin.__class__.__name__}' registered successfully.")
            if len(arguments) > 1:
                self.commands[plugin.__class__.__name__.lower()] = [plugin.__class__.__name__.lower(), f"No of Arguments is {len(arguments) - 1} & Arguments are {arguments[1:]}"]
            else:
                self.commands[plugin.__class__.__name__.lower()] = [plugin.__class__.__name__.lower(), f"No of Arguments is {len(arguments) - 1}"]
            

    def list_plugins(self):
        """List all available plugin commands."""
        return list(self.commands.keys())

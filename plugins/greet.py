# File: plugins/example_plugin.py

from plugin import Plugin  # Import the Plugin class from the plugin module

class GreetPlugin(Plugin):
    """An example plugin that provides additional functionality."""
    def execute(self,arg1,arg2):
        print(arg1,arg2)
        print("greet")
       

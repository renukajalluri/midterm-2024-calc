from commands import Command

class GreetPlugin(Command):
    """An example plugin that provides additional functionality."""

    command_name = "greet"
    @staticmethod
    def execute(arg1,arg2):
        print(arg1,arg2)
        print("greet")
       

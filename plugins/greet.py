from commands import Command

class GreetPlugin(Command):
    """An example plugin that provides additional functionality."""
    def execute(self,arg1,arg2):
        print(arg1,arg2)
        print("greet")
       

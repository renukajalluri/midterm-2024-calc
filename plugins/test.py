from commands import Command

class Test(Command):
    """An example plugin that provides additional functionality."""
    command_name = "test"
    

    @staticmethod
    def execute():
        print("testing")
       

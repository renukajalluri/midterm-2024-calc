
import logging
import os
from calculator import Calculator
from commands import CommandHandler


import sys
# Configure logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()  # Default to INFO if not set
LOG_FILE = os.getenv('LOG_FILE', 'calculator.log')  # Default log file name

logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),  # Log to a file
        logging.StreamHandler()  # Also log to the console
    ]
)


class App :
    def start(self):
            calculator = Calculator()
            commandHandler = CommandHandler()
            commandHandler.load_plugins("plugins")
            print(commandHandler.commands)
            logging.info("Application started. Type 'exit' to exit.")

            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)  # Use sys.exit(0) for a clean exit, indicating success.

                if len(cmd_input.split(" "))>1:
                    operation = cmd_input.split(" ")[0]
                    arguments = cmd_input.split(" ")[1:]
                else : 
                    operation = cmd_input.split(" ")[0]
                    arguments = []
                # looking for operation
                if operation == "add":
                    calculator.add(arguments[0], arguments[1])
                if operation == "subtract":
                    calculator.subtract(arguments[0], arguments[1])
                if operation == "multiply":
                    calculator.multiply(arguments[0], arguments[1])
                if operation == "divide":
                    calculator.divide(arguments[0], arguments[1])


                if operation in commandHandler.commands.keys():
                    commandHandler.commands[operation][0].execute(*arguments)


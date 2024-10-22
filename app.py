"""
A command-line calculator application with REPL (Read-Eval-Print Loop) functionality.

This module allows users to perform basic arithmetic operations (addition, subtraction, multiplication, division) and manage calculation history. It supports loading additional commands via plugins and logs interactions for debugging and monitoring.

Classes:
- App: The main application class that initializes the calculator, handles user input, and processes commands.
"""
import logging
import os
import logging.config
from dotenv import load_dotenv  # Third-party import
from calculator.calculator import Calculator  # First-party import
from commands import CommandHandler  # First-party import


class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.calculator = Calculator()
        self.commandHandler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)


    def repl(self):
         while True:
            try:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Exiting the calculator.")
                    print("Exiting the calculator.")
                    break

                if cmd_input.lower() == 'history':
                    print("Calculation History:")
                    print(self.calculator.show_history())
                    break
                
                if cmd_input.lower() == 'load_history':
                    logging.info("Loading history.")
                    print(self.calculator.load_history())
                    continue

                if cmd_input.lower() == "save_history":
                    logging.info("Saving history.")
                    print(self.calculator.save_history())
                    continue

                elif cmd_input.lower() == "clear_history":
                 logging.info("Clearing history.")
                 print(self.calculator.clear_history())
                 continue
                elif cmd_input.startswith("delete_history_record"):
                    cmd_parts = cmd_input.split()

                    if len(cmd_parts) == 2 and cmd_parts[1].isdigit():
                        index = int(cmd_parts[1])
                        logging.info("Deleting history record at index: %d", index)
                        print(self.calculator.delete_history_record(index))
                    else:
                        logging.warning("Invalid index provided for delete_history_record.")
                        print("Error: Please provide a valid index to delete.")
                    continue
                elif cmd_input.lower() == 'menu':
                    print("Available commands:")
                    print(self.commandHandler.list_plugins())
                # Split the command and its arguments
                cmd_parts = cmd_input.split()
                if len(cmd_parts) == 0:
                    logging.warning("No command entered.")
                    continue  # Skip iteration if no input

                operation = cmd_parts[0]
                arguments = cmd_parts[1:]

                # Handle built-in calculator operations
                if operation in ['add', 'subtract', 'multiply', 'divide']:
                    if len(arguments) != 2:
                        logging.error("%s requires exactly 2 arguments.", operation)
                        print(f"Error: {operation} requires exactly 2 arguments.")
                        continue

                    try:
                        # Convert arguments to numbers
                        arg1, arg2 = float(arguments[0]), float(arguments[1])
                    except ValueError:
                        logging.error("Invalid arguments. Arguments must be numbers.")
                        print("Error: Invalid arguments. Arguments must be numbers.")
                        continue

                    # Perform the operation and log results
                    if operation == "add":
                        result = self.calculator.add(arg1, arg2)
                    elif operation == "subtract":
                        result = self.calculator.subtract(arg1, arg2)
                    elif operation == "multiply":
                        result = self.calculator.multiply(arg1, arg2)
                    elif operation == "divide":
                        try:
                            result = self.calculator.divide(arg1, arg2)
                        except ZeroDivisionError:
                            logging.error("Division by zero error.")
                            print("Error: Division by zero is not allowed.")
                            continue

                    logging.info("Result of %s: %s", operation, result)
                    print(f"Result: {result}")

                # Handle plugin commands
                elif operation in self.commandHandler.commands.keys():
                    try:
                        self.commandHandler.commands[operation][0].execute(*arguments)
                    except Exception as e:
                        logging.error(f"Error executing command '{operation}': {e}")
                        print(f"Error: Failed to execute '{operation}'. {e}")

                if operation not in self.commandHandler.list_plugins() +  ['add', 'subtract', 'multiply', 'divide',"menu"]: 
                    print("command not found")
            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                print(f"Error: An unexpected error occurred: {e}")
    def start(self):    
        self.commandHandler.load_plugins("plugins")
        print(self.commandHandler.commands)
        logging.info("Calculator REPL started.")
        logging.info("Type 'exit' to exit.")
        print("Available history commands: load_history, save_history, clear_history, delete_history_record <index>.")
        self.repl()
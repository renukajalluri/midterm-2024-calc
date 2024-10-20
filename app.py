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


class App:
    def start(self):
        calculator = Calculator()
        commandHandler = CommandHandler()
        commandHandler.load_plugins("plugins")
        print(commandHandler.commands)
        logging.info("Application started. Type 'exit' to exit.")

        while True:
            try:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)  # Use sys.exit(0) for a clean exit, indicating success.

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
                        logging.error(f"{operation} requires exactly 2 arguments.")
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
                        result = calculator.add(arg1, arg2)
                    elif operation == "subtract":
                        result = calculator.subtract(arg1, arg2)
                    elif operation == "multiply":
                        result = calculator.multiply(arg1, arg2)
                    elif operation == "divide":
                        try:
                            result = calculator.divide(arg1, arg2)
                        except ZeroDivisionError:
                            logging.error("Division by zero error.")
                            print("Error: Division by zero is not allowed.")
                            continue

                    logging.info(f"Result of {operation}: {result}")
                    print(f"Result: {result}")

                # Handle plugin commands
                elif operation in commandHandler.commands.keys():
                    try:
                        commandHandler.commands[operation][0].execute(*arguments)
                    except Exception as e:
                        logging.error(f"Error executing command '{operation}': {e}")
                        print(f"Error: Failed to execute '{operation}'. {e}")

                else:
                    logging.error(f"Unknown command: {operation}")
                    print(f"Error: Unknown command '{operation}'.")

            except Exception as e:
                logging.error(f"An unexpected error occurred: {e}")
                print(f"Error: An unexpected error occurred: {e}")


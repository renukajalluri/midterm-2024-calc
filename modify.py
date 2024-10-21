# # File: main.py

# import logging
# import os
# from calculator import Calculator
# from plugin import PluginManager

# # Configure logging
# LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()  # Default to INFO if not set
# LOG_FILE = os.getenv('LOG_FILE', 'calculator.log')  # Default log file name

# logging.basicConfig(
#     level=LOG_LEVEL,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler(LOG_FILE),  # Log to a file
#         logging.StreamHandler()  # Also log to the console
#     ]
# )

# def repl():
#     """Read-Eval-Print Loop for interacting with the calculator."""
#     calculator = Calculator()
#     plugin_manager = PluginManager()
    
#     # Load plugins from the "plugins" directory
#     plugin_manager.load_plugins("plugins")
    
#     logging.info("Calculator REPL started.")
#     print("Type 'exit' to quit, 'history' to see calculation history, or 'menu' for available commands.")
#     print("Available history commands: load_history, save_history, clear_history, delete_history_record <index>.")

#     while True:
#         try:
            
#             user_input = input("Enter command: ")
#             parts = user_input.split()
#             logging.info(f"User input received: {user_input}")
#             if user_input.lower() == 'exit':
#                 logging.info("Exiting the calculator.")
#                 print("Exiting the calculator.")
#                 break
#             elif user_input.lower() == 'history':
#                 print("Calculation History:")
#                 print(calculator.show_history())
#                 continue
#             elif user_input.lower() == 'menu':
#                 print("Available commands:")
#                 print(calculator.list_plugins())
                
#                 for name, plugin in calculator.list_plugins().items():
#                     print(f" - {name} (Plugin: {plugin.__class__.__name__})")
#                 continue
            
#             # if parts[0] in calculator.list_plugins().keys():
#             #     calculator.list_plugins()[parts[0]].execute(*parts[1:])
#                             # Handle history management commands
            
#             if parts[0] == "load_history":
#                 logging.info("Loading history.")
#                 print(calculator.load_history())
#                 continue
#             elif parts[0] == "save_history":
#                 logging.info("Saving history.")
#                 print(calculator.save_history())
#                 continue
#             elif parts[0] == "clear_history":
#                 logging.info("Clearing history.")
#                 print(calculator.clear_history())
#                 continue
#             elif parts[0] == "delete_history_record":
#                 if len(parts) == 2 and parts[1].isdigit():
#                     index = int(parts[1])
#                     logging.info(f"Deleting history record at index: {index}")
#                     print(calculator.delete_history_record(index))
#                 else:
#                     logging.warning("Invalid index provided for delete_history_record.")
#                     print("Error: Please provide a valid index to delete.")
#                 continue
            
#             # Evaluate user input for arithmetic operations
#             # if len(parts) != 3:
#             #     logging.error("Invalid input format.")
#             #     print("Invalid input. Please enter: <operation> <num1> <num2>")
#             #     continue
            
#             operation, num1, num2 = parts[0], float(parts[1]), float(parts[2])
#             logging.info(f"Performing operation: {operation} with numbers: {num1}, {num2}")

#             if operation == "add":
#                 result = calculator.add(num1, num2)
#             elif operation == "subtract":
#                 result = calculator.subtract(num1, num2)
#             elif operation == "multiply":
#                 result = calculator.multiply(num1, num2)
#             elif operation == "divide":
#                 result = calculator.divide(num1, num2)
#             else:
#                 logging.error("Unknown operation requested.")
#                 print("Unknown operation. Please use add, subtract, multiply, or divide.")
#                 continue
            
#             print(f"Result: {result}")
#             logging.info(f"Operation result: {result}")
        
#         except ValueError as e:
#             logging.error(f"ValueError occurred: {e}")
#             print(f"Error: {e}")
#         # except Exception as e:
#         #     logging.error(f"Unexpected error occurred: {e}")
#         #     print(f"Unexpected error: {e}")

# if __name__ == "__main__":
#     repl()



from app import App


app = App()

app.start()
# File: main.py

from calculator import Calculator
from plugin import PluginManager

def repl():
    """Read-Eval-Print Loop for interacting with the calculator."""
    calculator = Calculator()
    plugin_manager = PluginManager(calculator)
    
    # Load plugins from the "plugins" directory
    plugin_manager.load_plugins("plugins")
    
    print("Welcome to the Calculator REPL!")
    print("Type 'exit' to quit, 'history' to see calculation history, or 'menu' for available commands.")
    print("Available history commands: load_history, save_history, clear_history, delete_history_record <index>.")

    while True:
        try:
            user_input = input("Enter command: ")
            if user_input.lower() == 'exit':
                print("Exiting the calculator.")
                break
            elif user_input.lower() == 'history':
                print("Calculation History:")
                print(calculator.show_history())
                continue
            elif user_input.lower() == 'menu':
                print("Available commands:")
                for name, plugin in calculator.list_plugins().items():
                    print(f" - {name} (Plugin: {plugin.__class__.__name__})")
                continue
            
            # Handle history management commands
            parts = user_input.split()
            if parts[0] == "load_history":
                print(calculator.load_history())
                continue
            elif parts[0] == "save_history":
                print(calculator.save_history())
                continue
            elif parts[0] == "clear_history":
                print(calculator.clear_history())
                continue
            elif parts[0] == "delete_history_record":
                if len(parts) == 2 and parts[1].isdigit():
                    index = int(parts[1])
                    print(calculator.delete_history_record(index))
                else:
                    print("Error: Please provide a valid index to delete.")
                continue
            
            # Evaluate user input for arithmetic operations
            if len(parts) != 3:
                print("Invalid input. Please enter: <operation> <num1> <num2>")
                continue
            
            operation, num1, num2 = parts[0], float(parts[1]), float(parts[2])
            
            if operation == "add":
                result = calculator.add(num1, num2)
            elif operation == "subtract":
                result = calculator.subtract(num1, num2)
            elif operation == "multiply":
                result = calculator.multiply(num1, num2)
            elif operation == "divide":
                result = calculator.divide(num1, num2)
            else:
                print("Unknown operation. Please use add, subtract, multiply, or divide.")
                continue
            
            print(f"Result: {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    repl()

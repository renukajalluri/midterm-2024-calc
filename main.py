class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"Added {a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"Subtracted {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"Multiplied {a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"Divided {a} / {b} = {result}")
        return result

    def show_history(self):
        return "\n".join(self.history)


def repl():
    calculator = Calculator()
    print("Welcome to the Calculator REPL!")
    print("Type 'exit' to quit or 'history' to see calculation history.")
    
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
            
            # Evaluate user input
            parts = user_input.split()
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

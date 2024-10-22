# Advanced Python Calculator for Software Engineering Graduate Course

This midterm requires the development of an advanced Python-based calculator application. Designed to underscore the importance of professional software development practices, the application integrates clean, maintainable code, the application of design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

# Getting Started

**Prerequisites:**
- Python 3.8 or higher
- pytest for running tests

**Installation:**

1. **Clone the repository:**:
```
git clone https://github.com/Hk574/Midterm-project.git
cd Midterm-project
```
2. **Create a virtual environment (optional but recommended):**:
```
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install the dependencies:**:
```
pip install -r requirements.txt
```

# Design Patterns Used:
1. **Facade Pattern:**: Implemented in the HistoryFacade class to simplify interactions with the history management functionalities. This pattern hides the complexities of the underlying operations (like adding, saving, loading, and clearing history) and provides a simplified interface.

Code: (https://github.com/Hk574/Midterm-project.git/calculator/history.py)

2. **Singleton Pattern:**: Used in the CommandHandlerFactory class to ensure that only one instance manages command registration and execution. This ensures consistent behavior across the application.

Code: (https://github.com/Hk574/Midterm-project.git/commands/__init__.py)

3. **Factory Method:**: The Factory Method pattern is implemented in the CommandHandlerFactory class, which dynamically loads and registers command plugins at runtime. This allows for the flexible addition of new commands by instantiating subclasses of the Command base class without modifying existing code, thus enhancing scalability and maintainability.

Code: (https://github.com/Hk574/Midterm-project.git/commands/__init__.py)


# Environment Variables

Usage of Environment Variables: Environment variables are loaded using the python-dotenv library to manage configurations such as logging levels and plugin paths. This keeps sensitive information out of the codebase and allows easy modifications without altering the code.

Link to Code: (https://github.com/Hk574/Midterm-project.git/.env)

# Logging Strategy
Logging Implementation: Logging is configured at the application startup to track user interactions and errors. It uses a logging configuration file (logging.conf) or defaults to basic configuration. Log messages provide insights into operational flows and errors encountered, aiding debugging and monitoring.

# Error Handling
The application implements two approaches for error handling:

**Easier to Ask for Forgiveness than Permission (EAFP):** Assumes operations will succeed and handles exceptions if they occur.

**Example:**

```python
try:
    self.command_handler.commands[operation][0].execute(*arguments)
except Exception as e:
    logging.error("Error executing command '%s': %s", operation, e)

```

**Look Before You Leap (LBYL):** Uses condition checks before performing actions (e.g., verifying command arguments).

**Example:**

```python
if len(arguments) != 2:
    logging.error("%s requires exactly 2 arguments.", operation)


Code: [app.py](https://github.com/Hk574/Midterm-project.git/app.py)

```

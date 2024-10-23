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

4. **Set up environment variables:**: Create a .env file in the project root and define any necessary variables, such as:

- ENVIRONMENT=PRODUCTION
- PLUGIN_FILE_PATH=plugins
- BOOKS_FILE_PATH=data/books.csv

# Usage Examples

1. **Run the application:**:

```
python app.py
```


2. **Basic commands:**:
- Add: ``` add 5 3 ```
- Subtract: ``` subtract 10 4 ```
- Divide: ``` divide 8 2 ```
- Exit: ``` exit ```
- View history: ``` history ```
- Save history: ``` save_history ```
- Load history: ``` load_history ```
- Clear history: ``` clear_history ```
- Delete history record:``` delete_history_record <index> ```
- Menu: ``` menu ```


# Calculator Class

The Calculator class performs basic arithmetic operations and manages calculation history through the HistoryFacade. Each operation logs the calculation to the history and records it for later retrieval.

# History Management

The HistoryFacade class manages calculation history using a Pandas DataFrame, allowing for adding, saving, loading, and clearing history entries.

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


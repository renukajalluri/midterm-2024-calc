Design Patterns

Design Patterns Used:

1. Facade Pattern: Implemented in the HistoryFacade class to simplify interactions with the history management functionalities. This pattern hides the complexities of the underlying operations (like adding, saving, loading, and clearing history) and provides a simplified interface.

Link to Code: calculator/history.py

2. Singleton Pattern: Used in the CommandHandler class to ensure that only one instance manages command registration and execution. This ensures consistent behavior across the application.

Link to Code: commands/__init__.py

Environment Variables

Usage of Environment Variables: Environment variables are loaded using the python-dotenv library to manage configurations such as logging levels and plugin paths. This keeps sensitive information out of the codebase and allows easy modifications without altering the code.

Link to Code: .env

Logging Strategy
Logging Implementation: Logging is configured at the application startup to track user interactions and errors. It uses a logging configuration file (logging.conf) or defaults to basic configuration. Log messages provide insights into operational flows and errors encountered, aiding debugging and monitoring.

Error Handling
The application implements two approaches for error handling:

Look Before You Leap (LBYL): Uses condition checks before performing actions (e.g., verifying command arguments).

Example:

if len(arguments) != 2:
    logging.error("%s requires exactly 2 arguments.", operation)

Link to code: app.py

Easier to Ask for Forgiveness than Permission (EAFP): Assumes operations will succeed and handles exceptions if they occur.

Example:

try:
    self.command_handler.commands[operation][0].execute(*arguments)
except Exception as e:
    logging.error("Error executing command '%s': %s", operation, e)

link to code: app.py
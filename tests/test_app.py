from unittest.mock import patch
import pytest

from app import App

@pytest.fixture
def app():
    """Fixture for creating an instance of the App."""
    return App()

def test_app_get_environment_variable():
    app = App()
#   Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    
    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_menu(app, monkeypatch, capsys):
    """Test the menu command."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    # Run the REPL
    with pytest.raises(SystemExit):
        app.start()

    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check if the expected output is present
    assert "Available commands:" in captured.out



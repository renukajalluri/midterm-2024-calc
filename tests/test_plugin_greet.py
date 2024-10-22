"""Test cases for the GreetPlugin execute method."""
import logging
from plugins.greet import GreetPlugin
# Test case for GreetPlugin
def test_greet_plugin_execute(capfd, caplog):
    """Test the execute method of GreetPlugin."""
    arg1 = "Hello"
    arg2 = "World"    
    # Capture the log output
    with caplog.at_level(logging.INFO):
        # Execute the greet command
        GreetPlugin.execute(arg1, arg2)

        # Capture the printed output
        out, _ = capfd.readouterr()

        # Verify the printed output
        assert "Hello World" in out
        assert "greet" in out

        # Verify the log output
        assert "greet" in caplog.text

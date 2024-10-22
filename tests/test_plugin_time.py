"""Test the TimePlugin's execute method for correct output and logging."""

import logging
from datetime import datetime

from plugins.time import TimePlugin

# Test case for TimePlugin
def test_time_plugin_execute(capfd, caplog):
    """Test the execute method of TimePlugin."""
    # Capture the log output
    with caplog.at_level(logging.INFO):
        # Execute the time command
        TimePlugin.execute()
        # Capture the printed output
        out, _ = capfd.readouterr()
        # Extract the current time format
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")        
        # Verify the printed output contains "Current Time" and the current time (ignoring seconds to avoid timing issues)
        assert "Current Time:" in out
        assert current_time in out

        # Verify the log output contains "Displayed current time"
        assert "Displayed current time:" in caplog.text

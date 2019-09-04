"""
Tests for file_processor.py
"""
import src.file_processor as processor

# @patch('src.commands.processor')
def test_read_file():

    assert processor.read_file("example.py") == {
        "lambda_handler": {
            "function_name": "lambda_handler",
            "logs": [
                {"type": "debug", "message": "Initialising"},
                {"type": "info", "message": "Processing"},
                {"type": "warn", "message": "Success"},
                {"type": "error", "message": "Failure"},
                {"type": "critical", "message": "Bananas"},
            ],
        }
    }

"""
Tests for file_processor.py
"""
import src.file_processor as processor


def test_read_file():

    assert processor.read_file("tests/unit/resources/example.py") == {
        "lambda_handler": {
            "function_name": "lambda_handler",
            "logs": [
                {"type": "debug", "filter": 'message: "Initialising"'},
                {"type": "info", "filter": 'message: "Processing"'},
                {"type": "warn", "filter": 'message: "Success"'},
                {"type": "error", "filter": 'message: "Failure"'},
                {"type": "critical", "filter": 'message: "Bananas"'},
            ],
        }
    }

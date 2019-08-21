import unittest
from unittest.mock import patch
import src.file_processor as file_processor


class TestFileProcessor(unittest.TestCase):

    # @patch('src.commands.processor')
    def test_read_file(self):

        self.assertEqual(
            file_processor.readFile("example.py"), {
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
            },
        )


if __name__ == "__name__":
    unittest.main()

"""
Tests for commands.py
"""

# import pytest
import src.commands as commands
from unittest.mock import patch
from pytest import mark


@patch.object(commands.processor, "read_file")
@mark.parametrize(
    "files, expected",
    [
        (["one"], 1),
        (["one", "two", "three"], 3),
    ]
)
def test_process_file(processor, files, expected):
    for fileName in files:
        commands.process_file(fileName)
    assert processor.call_count == expected


@patch.object(commands, "remove_functions_without_logs")
@patch.object(commands.processor, "read_file")
def test_process_and_generate_visualisations(read_file, remove_functions):
    commands.process_and_generate_visualisations("file")
    assert read_file.call_count == 1
    assert remove_functions.call_count == 1


# # #
# # Probably make this the "integration test"
# # #

# class TestCommands(unittest.TestCase):

#     def test_command_is_command(self):
# Test it with this http://click.palletsprojects.com/en/5.x/testing/
#

# if __name__ == '__name__':
#     unittest.main()

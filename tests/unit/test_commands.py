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


@patch.object(commands.kib, "generate_visualisation")
@patch.object(commands, "remove_functions_without_logs")
@patch.object(commands.processor, "read_file")
@mark.parametrize(
    "vis_generated, calls_expected",
    [
        ({}, 0),
        ({"key": "value"}, 1)
    ]
)
def test_process_and_generate_visualisations(read_file, remove_functions,
                                             generate_visualisation,
                                             vis_generated, calls_expected):
    remove_functions.return_value = vis_generated
    commands.process_and_generate_visualisations("file")
    assert read_file.call_count == 1
    assert remove_functions.call_count == 1
    assert generate_visualisation.call_count == calls_expected


@mark.parametrize(
    "processed_file, expected_result",
    [
        (dict({'name': {
            'function_name': 'name',
            'logs': [{
                'type': 'debug',
                'message': 'message'
            }]
        }}), {'name': {
            'function_name': 'name',
            'logs': [{
                'type': 'debug',
                'message': 'message'
            }]
        }}),
        ({'name': {
            'function_name': 'name',
            'logs': []
        }}, {})
    ]
)
def test_remove_functions_without_logs(processed_file, expected_result):
    expected_result == commands.remove_functions_without_logs(processed_file)

# # #
# # Probably make this the "integration test"
# # #

# class TestCommands(unittest.TestCase):

#     def test_command_is_command(self):
# Test it with this http://click.palletsprojects.com/en/5.x/testing/
#

# if __name__ == '__name__':
#     unittest.main()

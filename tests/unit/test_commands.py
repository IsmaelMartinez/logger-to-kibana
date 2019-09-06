"""
Tests for commands.py
"""

# import pytest
import src.commands as commands
from unittest.mock import patch


@patch.object(commands, "processor")
def test_process(commands):
    commands.process()


@patch.object(commands, "processor")
def test_process_and_generate(commands):
    commands.process_and_generate()

# import unittest
# from src.commands import commands
# # #
# # Probably make this the "integration test"
# # #

# class TestCommands(unittest.TestCase):

#     def test_command_is_command(self):
# Test it with this http://click.palletsprojects.com/en/5.x/testing/
#

# if __name__ == '__name__':
#     unittest.main()

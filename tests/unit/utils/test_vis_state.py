"""
Tests for vis_state.py
"""
import json
import os
from pytest import mark, raises
from src.utils.vis_state import VisState


@mark.parametrize(
    "input,expected", [("Tost", "[Generated] - Tost"), ("Test", "[Generated] - Test")]
)
def test_contructor(inp, expected):
    assert expected == VisState(inp).visState["title"]


def test_contructor_value_error():
    with raises(ValueError):
        VisState(None)


def test_add_value_error():
    vis = VisState("Valid")
    with raises(ValueError):
        vis.add(None)


@mark.parametrize(
    "input,expected",
    [("", "empty_vis_state_results.json"), ("Valid", "valid_vis_state_results.json")],
)
def test_get(inp, expected):
    assert get_test_results_json_file(expected) == VisState(inp).get()


@mark.parametrize(
    "input,expected",
    [("One", "one_vis_state_results.json"), ("Two", "two_vis_state_results.json")],
)
def test_add_one(inp, expected):
    vis = VisState("Valid")
    vis.add(inp)
    assert get_test_results_json_file(expected) == vis.get()


def get_test_results_json_file(name: str) -> dict:
    with open(os.path.abspath(f'tests/unit/resources/' + name)) as file:
        return json.loads(file.read())

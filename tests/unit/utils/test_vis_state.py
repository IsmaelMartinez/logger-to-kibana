"""
Tests for vis_state.py
"""
import json
import os
from pytest import mark, raises
from unittest.mock import patch
from src.utils.vis_state import VisState


@mark.parametrize(
    "key, logs, expected",
    [
        ("Tost", [], "[Generated] - Tost"),
        ("Test", [],  "[Generated] - Test")
    ]
)
def test_contructor(key, logs, expected):
    assert expected == VisState(key, logs).visState["title"]


@mark.parametrize(
    "key,expected",
    [
        ("Tost", "[Generated] - Tost"),
        ("Test", "[Generated] - Test")
    ]
)
def test_set_title(key, expected):
    vis_state = VisState(key, [])
    assert expected == vis_state.visState["title"]


def test_set_title_value_error():
    with raises(ValueError):
        VisState(None, [])


@patch.object(VisState, "add")
@mark.parametrize(
    "logs, expected",
    [
        ([{'message': 'Test'}], 1),
        ([{'message': 'Test'}, {'message': 'Test2'}, {'message': 'Test3'}], 3)
    ]
)
def test_set_logs(add, logs, expected):
    vis_state = VisState("Test", [])
    vis_state.set_logs(logs)
    assert add.call_count == expected


def test_add_value_error():
    vis = VisState("Valid", [])
    with raises(ValueError):
        vis.add(None)


@mark.parametrize(
    "key,expected",
    [
        ("", "empty_vis_state_results.json"),
        ("Valid", "valid_vis_state_results.json")
    ],
)
def test_get(key, expected):
    assert get_test_results_json_file(expected) == VisState(key, []).get()


@mark.parametrize(
    "key,expected",
    [
        (["One"], "one_vis_state_results.json"),
        (["One", "Two"], "two_vis_state_results.json")
    ],
)
def test_add_one(key, expected):
    vis = VisState("Valid", [])
    for value in key:
        vis.add(value)
    assert get_test_results_json_file(expected) == vis.get()


def get_test_results_json_file(name: str) -> dict:
    with open(os.path.abspath(f"tests/unit/resources/" + name)) as file:
        return json.loads(file.read())

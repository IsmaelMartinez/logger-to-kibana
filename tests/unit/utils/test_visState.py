from pytest import mark, raises
from src.utils.visState import VisState
import os
import json


@mark.parametrize("input,expected",
    [
        ("Tost", '[Generated] - Tost'),
        ("Test", '[Generated] - Test'),
    ])
def test_contructor(input, expected):
    assert expected == VisState(input).visState['title']

def test_contructor_value_error():
    with raises(ValueError):
        VisState(None)

# @mark.parametrize("input,expected",
#     [
#         (["One"], "one_visState_results.json"),
#         # (["One","Two"], "two_visState_results.json"),
#     ])

def test_add_value_error():
    vis = VisState("Valid")
    with raises(ValueError):
        vis.add(None)

@mark.parametrize("input,expected",
    [
        ("", "empty_visState_results.json"),
        ("Valid", "valid_visState_results.json")
    ])
def test_get(input, expected):
    assert get_test_results_json_file(expected) == VisState(input).get()

@mark.parametrize("input,expected",
    [
        ("One", "one_visState_results.json"),
        ("Two", "two_visState_results.json"),
    ])
def test_add_one(input, expected):
    vis = VisState("Valid")
    vis.add(input)
    assert get_test_results_json_file(expected) == vis.get()

def get_test_results_json_file(name: str) -> dict:
    with open(os.path.abspath(f"tests/unit/resources/"+name)) as f:
        return json.loads(f.read())

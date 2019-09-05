import os
import json
from src.utils.visualisation import Visualisation
from pytest import mark, raises


@mark.parametrize(
    "key, vis_state, expected",
    [
        ("", {}, "visualisation_with_empty_vis_state.json"),
        ("Valid", {"some": "here"}, "visualisation_with_valid_values.json")
    ]
)
def test_constructor(key, vis_state, expected):
    assert get_test_results_json_file(expected) == \
        Visualisation(key, vis_state).visualisation


def test_set_title_value_error():
    visualisation = Visualisation("Test", {})
    with raises(ValueError):
        visualisation.set_title(None)


@mark.parametrize(
    "title, expected",
    [
        ("One", "[Generated] - One"),
        ("fsdfasfd", "[Generated] - fsdfasfd")
    ]
)
def test_set_title(title, expected):
    visualisation = Visualisation("Test", {})
    assert visualisation.visualisation['title'] == "[Generated] - Test"
    visualisation.set_title(title)
    assert visualisation.visualisation['title'] == expected


def test_set_vis_state_value_error():
    visualisation = Visualisation("Test", {})
    with raises(ValueError):
        visualisation.set_vis_state(None)


@mark.parametrize(
    "vis_state, expected",
    [
        ({}, "{}"),
        ({"some": "stuff"}, "{\"some\": \"stuff\"}")
    ]
)
def test_set_vis_state(vis_state, expected):
    visualisation = Visualisation("Test", {})
    assert visualisation.visualisation['visState'] == "{}"
    visualisation.set_vis_state(vis_state)
    assert visualisation.visualisation['visState'] == expected


@mark.parametrize(
    "key, vis_state, expected",
    [
        ("", {}, "visualisation_with_empty_vis_state.json"),
        ("Valid", {"some": "here"}, "visualisation_with_valid_values.json")
    ]
)
def test_get(key, vis_state, expected):
    assert get_test_results_json_file(expected) == \
        Visualisation(key, vis_state).get()


def get_test_results_json_file(name: str) -> dict:
    with open(os.path.abspath(f"tests/unit/resources/" + name)) as file:
        return json.loads(file.read())

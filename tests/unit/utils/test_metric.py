import json
import os
from pytest import mark, raises
from unittest.mock import patch
from src.utils import metric


@patch.object(metric, "set_logs")
@patch.object(metric, "set_title")
def test_generate_metric_vis_state(set_title, set_logs):
    metric.generate_metric_vis_state("bfk", ["bla"])
    assert set_title.call_count == 1
    assert set_logs.call_count == 1


def test_generate_metric_vis_state_integration():
    query = [{"query": "One", "label": "One"},
             {"query": "Two", "label": "Two"}]
    assert metric.generate_metric_vis_state("Valid", query) == \
        get_test_results_json_file("valid_vis_state_results.json")


def test_set_title_value_error():
    with raises(ValueError):
        metric.set_title(None)


@mark.parametrize(
    "path_name, expected",
    [
        ("path", "[Generated] - path"),
        ("pfdsafdsa ", "[Generated] - pfdsafdsa "),
        ("", "[Generated] - ")
    ]
)
def test_set_title(path_name, expected):
    metric.set_title(path_name)
    assert metric.vis_state["title"] == expected


@mark.parametrize(
    "logs, expected",
    [
        (None, "empty_vis_state_results.json"),
        ([],
         "empty_vis_state_results.json"),
        ([{"query": "one", "label": "one"}],
         "one_vis_state_results.json"),
        ([{"query": "One", "label": "One"}, {"query": "Two", "label": "Two"}],
         "two_vis_state_results.json")
    ],
)
def test_set_logs(logs, expected):
    metric.set_logs(logs)
    assert get_test_results_json_file(expected) == metric.vis_state



# @mark.parametrize(
#     "project, key, logs, expected",
#     [
#         ("Project", "Tost", [], "[Generated] - Project - Tost"),
#         ("Project", "Test", [], "[Generated] - Project - Test")
#     ]
# )
# def test_contructor(project, key, logs, expected):
#     assert expected == VisState(project, key, logs).visState["title"]



# @mark.parametrize(
#     "key,expected",
#     [
#         (["One"], "one_vis_state_results.json"),
#         (["One", "Two"], "two_vis_state_results.json")
#     ],
# )
# def test_add_one(key, expected):
#     vis = VisState("", "Valid", [])
#     for value in key:
#         vis.add(value)
#     assert get_test_results_json_file(expected) == vis.get()


def get_test_results_json_file(name: str) -> dict:
    with open(os.path.abspath(f"tests/unit/resources/" + name)) as file:
        return json.loads(file.read())

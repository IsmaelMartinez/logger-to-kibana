import pytest
import src.kibana as kib
from unittest.mock import patch


@patch.object(kib, "requests")
@pytest.mark.parametrize(
    "project, key, value, expected",
    [
        ("A", "title", {"logs": []}, {})
    ]
)
def test_generate_visualisation(requests, project, key, value, expected):
    expected == kib.generate_visualisation(project, key, value)

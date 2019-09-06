import pytest
import src.kibana as kib
from unittest.mock import patch


@patch.object(kib, "requests")
@pytest.mark.parametrize(
    "key, value, expected",
    [
        # (None, None, None),
        ("title", {"logs": []}, {})
    ]
)
def test_generate_visualisation(requests, key, value, expected):
    expected == kib.generate_visualisation(key, value)

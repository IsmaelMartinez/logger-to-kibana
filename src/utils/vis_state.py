"""
This module handles the Metric visualisation generation
"""
import copy


class VisState:
    """
    VisState handles the generation of Metric Visualisation Objects
    that follow the Kibana format
    """

    metricGroupFilter = {"input": {"query": ""}, "label": ""}

    visState = {
        "title": "",
        "type": "metric",
        "params": {
            "addTooltip": True,
            "addLegend": False,
            "type": "metric",
            "metric": {
                "percentageMode": False,
                "useRanges": False,
                "colorSchema": "Green to Red",
                "metricColorMode": "None",
                "colorsRange": [{"from": 0, "to": 10000}],
                "labels": {"show": True},
                "invertColors": False,
                "style": {
                    "bgFill": "#000",
                    "bgColor": False,
                    "labelColor": False,
                    "subText": "",
                    "fontSize": 60,
                },
            },
        },
        "aggs": [
            {
                "id": "1",
                "enabled": True,
                "type": "count",
                "schema": "metric",
                "params": {},
            },
            {
                "id": "2",
                "enabled": True,
                "type": "filters",
                "schema": "group",
                "params": {"filters": []},
            },
        ],
    }

    def __init__(self, key: str, logs: []):
        self.reset()
        self.set_title(key)
        self.set_logs(logs)

    def set_title(self, key: str):
        if not isinstance(key, str):
            raise ValueError("key must be a string")
        self.visState["title"] = "[Generated] - " + str(key)

    def set_logs(self, logs: []):
        for i in range(len(logs)):
            self.add(logs[i]["message"])

    def add(self, log_message: str):
        """
        Add a new metric object that will search for the log_message provided
        """
        if not isinstance(log_message, str):
            raise ValueError("log_message must be a string")
        self.metricGroupFilter["input"]["query"] = log_message
        self.visState["aggs"][1]["params"]["filters"].append(
            copy.deepcopy(self.metricGroupFilter)
        )

    def reset(self):
        self.visState["title"] = ""
        self.visState["aggs"][1]["params"]["filters"] = []

    def get(self):
        """
        Get the visState object.
        """
        return self.visState

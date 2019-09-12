"""
This module handles the Metric Visualisation generation
"""
import copy


class VisState:
    """
    VisState handles the generation of Metric Visualisation Objects
    that follow the Kibana format
    """

    def __init__(self, project: str, key: str, logs: []):
        self.metricGroupFilter = {"input": {"query": ""}, "label": ""}
        self.visState = {
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

        self.set_title(project, key)
        self.set_logs(logs)

    def set_title(self, project: str, key: str):
        if not isinstance(project, str):
            raise ValueError("project must be a string")
        if not isinstance(key, str):
            raise ValueError("key must be a string")
        self.visState["title"] = f"[Generated] - {project} - {key}"

    def set_logs(self, logs: []):
        for i in range(len(logs)):
            self.add(logs[i]["filter"])

    def add(self, log_message: str):
        if not isinstance(log_message, str):
            raise ValueError("log_message must be a string")
        self.metricGroupFilter["input"]["query"] = log_message
        self.visState["aggs"][1]["params"]["filters"].append(
            copy.deepcopy(self.metricGroupFilter)
        )

    def get(self):
        return self.visState

import copy
import json

metricGroupFilter = {
    "input": {
        "query": ""
    },
    "label": ""
}

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
            "colorsRange": [
                {
                    "from": 0,
                    "to": 10000
                }
            ],
            "labels": {
                "show": True
            },
            "invertColors": False,
            "style": {
                "bgFill": "#000",
                "bgColor": False,
                "labelColor": False,
                "subText": "",
                "fontSize": 60
            }
        }
    },
    "aggs": [
        {
            "id": "1",
            "enabled": True,
            "type": "count",
            "schema": "metric",
            "params": {}
        },
        {
            "id": "2",
            "enabled": True,
            "type": "filters",
            "schema": "group",
            "params": {
                "filters": [

                ]
            }
        }
    ]
}

class VisState:
    def __init__(self, key):
        visState['title'] = '[Generated] - ' + key

    def add(self, log_message):
        metricGroupFilter['input']['query'] = log_message
        visState['aggs'][1]['params']['filters'].append(copy.deepcopy(metricGroupFilter))

    def get(self):
        return visState
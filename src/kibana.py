import requests
import json
import copy

visualization = {
    "title": ""
    "visState"
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

kibanaSavedObjectMeta = {
    "searchSourceJSON" : json.dumps({
    "index": "da4a6380-c1f4-11e9-9258-a752fa2ba2cb",
    "query": {
        "query": "",
        "language": "lucene"
    },
    "filter": []
    })
}

metricGroupFilter = {
    "input": {
        "query": ""
    },
    "label": ""
}

def generate_visualisation(key: str, values: dict):
    visualization['title'] = '[Generated] - '+key
    visState['title'] = '[Generated] - '+key

    logs = values['logs']
    for i in range(len(logs)):
        metricGroupFilter['input']['query'] = logs[i]['message']
        print(metricGroupFilter)
        visState['aggs'][1]['params']['filters'].append(copy.deepcopy(metricGroupFilter))

    visualization['visState'] = json.dumps(visState)
    visualization['kibanaSavedObjectMeta'] = kibanaSavedObjectMeta

    print(visualization)

    headers = {"kbn-xsrf": "true"}
    data = {"attributes" : visualization}
    r = requests.post(
        f'http://localhost:5601/api/saved_objects/visualization/generated-{key}?overwrite=true',
        headers=headers,
        data=json.dumps(data))
    print(r.text)


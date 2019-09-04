import json

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

visualisation = {
    "title": ""
    "visState"
}

class Visualisation:
    def __init__(self, key, visState):
        visualisation['title'] = '[Generated] - ' + key
        visualisation['visState'] = json.dumps(visState)
        visualisation['kibanaSavedObjectMeta'] = kibanaSavedObjectMeta
        print(visualisation)

    def get(self):
        return visualisation

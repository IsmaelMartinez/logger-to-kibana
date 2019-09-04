import requests
import json
from src.utils import visualisation, visState


def generate_visualisation(key: str, values: dict):
    state = visState.VisState(key)

    logs = values['logs']
    for i in range(len(logs)):
        state.add(logs[i]['message'])

    vis = visualisation.Visualisation(key, state.get())

    headers = {"kbn-xsrf": "true"}
    data = {"attributes" : vis.get()}
    r = requests.post(
        f'http://localhost:5601/api/saved_objects/visualization/generated-{key}?overwrite=true',
        headers=headers,
        data=json.dumps(data))
    print(r.text)


"""
This function handles the generation of the kibana visualisation
"""
import json
import requests
from src.utils import visualisation, vis_state


def generate_visualisation(key: str, values: dict):
    """
    Generates the visualisation using the key and values provided
    """
    state = vis_state.VisState(key)

    logs = values["logs"]
    for i in range(len(logs)):
        state.add(logs[i]["message"])

    vis = visualisation.Visualisation(key, state.get())

    headers = {"kbn-xsrf": "true"}
    data = {"attributes": vis.get()}
    baseUrl = "http://localhost:5601"
    url = f"{baseUrl}/api/saved_objects/visualization/generated-{key}\
        ?overwrite=true"

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(data),
    )
    print(response.text)

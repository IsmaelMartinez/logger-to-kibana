"""
This function handles the generation of the kibana visualisation
"""
import configparser
import json
import requests
from src.utils import visualisation, vis_state

config = configparser.ConfigParser()
config.read("settings.ini")

baseUrl = config.get('kibana', 'BaseUrl')


def generate_visualisation(project: str, key: str, values: dict):
    """
    Generates the visualisation using the key and values provided
    """
    state = vis_state.VisState(project, key, values["logs"])

    vis = visualisation.Visualisation(project, key, state.get())

    headers = {"kbn-xsrf": "true"}
    data = {"attributes": vis.get()}
    url = (
        f"""{baseUrl}/api/saved_objects/visualization/"""
        f"""generated-{project}-{key}?overwrite=true"""
    )

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(data),
    )
    print(response.text)

"""
This function handles the generation of the kibana visualisation
"""
import configparser
import json
import requests
from pathlib import Path
from src.utils import visualisation, table

config = configparser.ConfigParser()
config.read("settings.ini")

baseUrl = config.get('kibana', 'BaseUrl')


def generate_and_send_visualisation(path_name: str, items: []):
    folder_name = Path(path_name).parts[-1]
    vis = generate_folder_visualisation(folder_name, items)
    send_visualisation(folder_name, vis)


def generate_folder_visualisation(folder_name: str, items: []) -> dict:
    metric = table.generate_metric_vis_state(folder_name, items)
    return visualisation.generate_visualisation(folder_name, metric)


def send_visualisation(folder_name: str, visualisation: dict):
    # import pdb; pdb.set_trace()
    headers = {"kbn-xsrf": "true"}
    data = {"attributes": visualisation}
    url = (
        f"""{baseUrl}/api/saved_objects/visualization/"""
        f"""generated-{folder_name}?overwrite=true"""
    )

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(data),
    )
    print(response.text)

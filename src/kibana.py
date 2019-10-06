"""
This function handles the generation of the kibana visualization
"""
from src.configuration import config

import json
import requests
from src.utils import visualization


def generate_and_send_visualization(folder_name: str, items: []):
    vis = generate_folder_visualization(folder_name, items)
    send_visualization(folder_name, vis)


def generate_folder_visualization(folder_name: str, items: []) -> dict:
    #https://docs.python.org/3/library/itertools.html#itertools.groupby
    return visualization.generate_visualization(folder_name, items)


def send_visualization(folder_name: str, visualization: dict):
    headers = {"kbn-xsrf": "true"}
    data = {"attributes": visualization}
    url = (
        f"""{config.kibana.BaseUrl}/api/saved_objects/visualization/"""
        f"""generated-{folder_name}?overwrite=true"""
    )

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(data),
    )
    print(response.text)

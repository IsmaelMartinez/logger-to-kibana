"""
This module handles the Kibana Visualisation generation
"""
import configparser
import json

config = configparser.ConfigParser()
config.read("settings.ini")

index = config.get('kibana', 'Index')


class Visualisation:
    """
    Visualisation handles the basic structure for kibana visualisations
    """

    def __init__(self, project: str, key: str, vis_state: dict):
        self.visualisation = {"title": "" "visState"}
        self.kibana_meta = {
            "searchSourceJSON": json.dumps(
                {
                    "index": index,
                    "query": {"query": "", "language": "lucene"},
                    "filter": [],
                }
            )
        }
        self.set_title(project, key)
        self.set_vis_state(vis_state)
        self.visualisation["kibanaSavedObjectMeta"] = self.kibana_meta

    def set_title(self, project: str, key: str):
        if not isinstance(project, str):
            raise ValueError("Project should be a string")
        if not isinstance(key, str):
            raise ValueError("Key should be a string")
        self.visualisation["title"] = "[Generated] - " + project + " - " + key

    def set_vis_state(self, vis_state: dict):
        if not isinstance(vis_state, dict):
            raise ValueError("vis_state should be a dict")
        self.visualisation["visState"] = json.dumps(vis_state)

    def get(self):
        return self.visualisation

"""
This module handles the Kibana VISUALISATION generation
"""
import json


class Visualisation:
    """
    Visualisation handles the basic structure for kibana visualisations
    """

    def __init__(self, key: str, vis_state: dict):
        self.visualisation = {"title": "" "visState"}
        self.kibana_meta = {
            "searchSourceJSON": json.dumps(
                {
                    "index": "90943e30-9a47-11e8-b64d-95841ca0b247",
                    "query": {"query": "", "language": "lucene"},
                    "filter": [],
                }
            )
        }
        self.set_title(key)
        self.set_vis_state(vis_state)
        self.visualisation["kibanaSavedObjectMeta"] = self.kibana_meta

    def set_title(self, key: str):
        """
        Sets the visualisation title
        """
        if not isinstance(key, str):
            raise ValueError("Key should be a string")
        self.visualisation["title"] = "[Generated] - " + key

    def set_vis_state(self, vis_state: dict):
        """
        Sets the visualisation visState object
        """
        if not isinstance(vis_state, dict):
            raise ValueError("vis_state should be a dict")
        self.visualisation["visState"] = json.dumps(vis_state)

    def get(self):
        """
        Returns the visualisation object
        """
        return self.visualisation

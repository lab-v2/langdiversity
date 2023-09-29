from typing import List, Dict, Union

import json

class PromptSelection:
    def __init__(self, data: List[Dict[str, Union[str, List[str], float]]], selection: str = "min"):
        valid_selections = ["min", "max"]
        if selection not in valid_selections:
            raise ValueError(
                "Invalid selection type. Expected one of %s" % valid_selections
            )
        self.data = data
        self.selection = selection

    def select(self):
        if not self.data:
            raise ValueError("No data to select from.")

        # Determine the target diversity value based on the selection type
        if self.selection == "min":
            target_diversity = min(item['diversity'] for item in self.data)
        else:
            target_diversity = max(item['diversity'] for item in self.data)

        # Filter the data list to return all items with the target diversity value
        selected_items = [item for item in self.data if item['diversity'] == target_diversity]

        # Prepare a dictionary to hold the selected prompts and diversity value
        results = {
            "selected_prompts": [item['prompt'] for item in selected_items],
            "diversity": target_diversity
        }

        return results 


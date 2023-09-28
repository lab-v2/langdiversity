from typing import List, Dict, Union

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

        selected_item = min(self.data, key=lambda x: x['diversity']) if self.selection == "min" else max(self.data, key=lambda x: x['diversity'])
        return selected_item['prompt'], selected_item['diversity']

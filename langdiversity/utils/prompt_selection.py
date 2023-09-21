from typing import List

from langdiversity.extras.spinner import loading_spinner

from langdiversity.measures import AbstractMeasure
from langdiversity.models import AbstractBaseModel

class PromptSelection:
    def __init__(
        self,
        model: AbstractBaseModel,
        diversity_measure: AbstractMeasure,
        num_responses: int = 1,
        selection: str = "min",
    ):
        valid_selections = ["min", "max"]
        if selection not in valid_selections:
            raise ValueError(
                "Invalid selection type. Expected one of %s" % valid_selections
            )
        self.model = model
        self.diversity_measure = diversity_measure
        self.num_responses = num_responses
        self.selection = selection

    def generate(self, prompts: List[str]):
        if len(prompts) == 0:
            raise ValueError("Invalid prompts. There should be at least 1 prompt.")

        selected_prompt = ""
        selected_diversity = float("inf") if self.selection == "min" else float("-inf")

        info = []

        total_prompts = len(prompts)
        for i, prompt in enumerate(prompts):
            with loading_spinner(f"Collecting {self.num_responses} responses...", current_step=i+1, total_steps=total_prompts):
                responses = self.model.generate(prompt, self.num_responses)
            with loading_spinner("Performing diversity measure calculations...", current_step=i+1, total_steps=total_prompts):
                diversity = self.diversity_measure.generate(responses)

            if self.selection == "max" and diversity > selected_diversity:
                selected_diversity = diversity
                selected_prompt = prompt
            if self.selection == "min" and diversity < selected_diversity:
                selected_diversity = diversity
                selected_prompt = prompt

            info.append(
                {"responses": responses, "diversity": diversity, "prompt": prompt}
            )

        return selected_prompt, selected_diversity

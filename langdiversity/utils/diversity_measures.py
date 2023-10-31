from typing import List

from langdiversity.extras.spinner import loading_spinner

from langdiversity.measures import AbstractMeasure
from langdiversity.models import AbstractBaseModel

class DiversityMeasureCollector:
    def __init__(self, model: AbstractBaseModel, diversity_measure: AbstractMeasure, num_responses: int = 1):
        self.model = model
        self.diversity_measure = diversity_measure
        self.num_responses = num_responses
        self.data = []  # A list to store the data (prompt, responses, diversity measure)

    def collect(self, prompts: List[str], verbose: bool = False):
        total_prompts = len(prompts)
        for i, prompt in enumerate(prompts):
            with loading_spinner(f"Collecting {self.num_responses} responses...", current_step=i + 1, total_steps=total_prompts):
                responses = self.model.generate(prompt, self.num_responses)
            with loading_spinner("Performing diversity measure calculations...", current_step=i + 1, total_steps=total_prompts):
                diversity = self.diversity_measure.generate(responses)
            if verbose:
                print(f"Responses: {', '.join(responses)}")  
                print(f"Diversity Measure ({self.diversity_measure.__class__.__name__}): {diversity}")
            self.data.append(
                {"prompt": prompt, "responses": responses, "diversity": diversity}
            )

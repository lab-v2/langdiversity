from typing import List

from diversity_measures.measures import AbstractMeasure
from diversity_measures.models import AbstractBaseModel

# class PromptSelection:
#     def __init__(self):
#         pass

#     def find_extreme_scores(self, all_scores, measures, selection_method='max'):
#         extreme_values = {}

#         for measure in measures:
#             scores_for_measure = [score[measure] for score in all_scores]

#             if selection_method == 'max':
#                 extreme_values[measure] = max(scores_for_measure)
#             elif selection_method == 'min':
#                 extreme_values[measure] = min(scores_for_measure)

#         return extreme_values


class PromptSelection:
    def __init__(
        self,
        model: AbstractBaseModel,
        diversity_measure: AbstractMeasure,
        num_responses: int = 1,
        selection: str = "max",
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
        for prompt in prompts:
            responses = self.model.generate(prompt, self.num_responses)
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

        return selected_prompt, selected_diversity, info

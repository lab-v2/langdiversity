from langdiversity.extras.spinner import loading_spinner
from ..measures import ShannonEntropyMeasure, GiniImpurityMeasure

class DiversityCalculator:
    def __init__(self, measures=["entropy"]):
        self.measures = measures
        self.measure_classes = {
            'entropy': ShannonEntropyMeasure,
            'gini': GiniImpurityMeasure,
        }

    def calculate(self, values):
        measures = self.measures

        results = {}

        for measure_name in measures:
            measure_class = self.measure_classes.get(measure_name)
            if measure_class is not None:
                measure_instance = measure_class()
                with loading_spinner(f"Calculating '{measure_name}' for {len(values)} values..."):
                    results[measure_name] = measure_instance.generate(values)

        return results

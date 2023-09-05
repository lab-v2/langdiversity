from ..measures import ShannonEntropyMeasure, GiniImpurityMeasure

class DiversityCalculator:
    def __init__(self, default_measures=["entropy"]):
        self.default_measures = default_measures

    def calculate(self, values, measures=None):
        if measures is None:
            measures = self.default_measures

        results = {}
        
        if "entropy" in measures:
            entropy_measure = ShannonEntropyMeasure()
            results["entropy"] = entropy_measure.generate(values)
        
        if "gini" in measures:
            gini_measure = GiniImpurityMeasure()
            results["gini_impurity"] = gini_measure.generate(values)
        
        return results
    

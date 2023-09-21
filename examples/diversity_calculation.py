from langdiversity.utils import DiversityCalculator
from langdiversity.measures import ShannonEntropyMeasure, GiniImpurityMeasure

# Define a custom measure class
class CustomMeasure:
    def generate(self, values):
        return sum(values) // len(values)

# Create instances
entropy = ShannonEntropyMeasure()
gini = GiniImpurityMeasure()
custom = CustomMeasure()

# Use built-in and custom measures
diversity_calculator = DiversityCalculator(measures=[entropy, gini, custom])

print("Diversity Measures:", diversity_calculator.calculate([1, 1, 1, 2]))

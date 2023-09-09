from langprobe.utils import DiversityCalculator

# Calculate diversity measures
diversity_calculator = DiversityCalculator(default_measures=["entropy", "gini"])
print("DIVERSITY MEASURES:", diversity_calculator.calculate([1, 1, 1, 2]))

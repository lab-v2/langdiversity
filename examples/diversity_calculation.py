from langdiversity.utils import DiversityCalculator

# Calculate diversity measures
diversity_calculator = DiversityCalculator(measures=["entropy", "gini"])
print("DIVERSITY MEASURES:", diversity_calculator.calculate([1, 1, 1, 2]))

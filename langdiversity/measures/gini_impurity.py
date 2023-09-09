from typing import List, Hashable

from .empirical_probability import empirical_probability
from .abstract_measure import AbstractMeasure

class GiniImpurityMeasure(AbstractMeasure):
    def generate(self, values: List[Hashable]) -> float:
        probabilities = empirical_probability(values=values)
        gini_impurity = 1 - sum(probability ** 2 for probability in probabilities.values())
        return gini_impurity
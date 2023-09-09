from math import log2
from typing import List, Hashable

from .empirical_probability import empirical_probability
from .abstract_measure import AbstractMeasure

class ShannonEntropyMeasure(AbstractMeasure):
    def generate(self, values: List[Hashable]) -> float:
        probabilities = empirical_probability(values=values)
        entropy = -sum(probability * log2(probability) for probability in probabilities.values() if probability > 0)
        return entropy
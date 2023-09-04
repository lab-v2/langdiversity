from collections import Counter
from typing import List, Hashable

def empirical_probability(values: List[Hashable]) -> List[float]:
    """
    Calculates the probability that a discrete random variable will take 
    on a particular value for each unique value in the list.
    """
    value_counts = Counter(values)
    total_elements = len(values)
    probabilities = {value: count / total_elements for value, count in value_counts.items()}
    return probabilities
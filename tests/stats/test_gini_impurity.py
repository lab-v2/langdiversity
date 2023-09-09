import unittest

from langdiversity.measures import GiniImpurityMeasure

class TestGiniImpurityMeasure(unittest.TestCase):
    def test_basic(self):
        shannon_entropy_measure = GiniImpurityMeasure()
        output = shannon_entropy_measure.generate(values=[5, 5, 5, 4.5, 3])
        self.assertAlmostEqual(output, 0.5599999999999999)
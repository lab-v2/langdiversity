import unittest

from langdiversity.measures import ShannonEntropyMeasure

class TestShannonEntropyMeasure(unittest.TestCase):
    def test_basic(self):
        shannon_entropy_measure = ShannonEntropyMeasure()
        output = shannon_entropy_measure.generate(values=[5, 5, 5, 4.5, 3])
        self.assertAlmostEqual(output, 1.370950594454669)
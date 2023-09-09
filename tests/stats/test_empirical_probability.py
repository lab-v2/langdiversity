import unittest

from langdiversity.measures import empirical_probability

class TestEmpiricalProbability(unittest.TestCase):
    def test_basic(self):
        output = empirical_probability([1, 1, 1, 2, 2])
        self.assertEqual(output, {1: 0.6, 2: 0.4})

    def test_single_distinct_value(self):
        output = empirical_probability([1, 1, 1, 1, 1])
        self.assertEqual(output, {1: 1})

    def test_empty_array(self):
        output = empirical_probability([])
        self.assertEqual(output, {})
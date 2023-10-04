import unittest

from llm_utils import llm_utils

class TestStringMethods(unittest.TestCase):
    def test_calculate_cost(self):
        self.assertAlmostEqual(llm_utils.calculate_cost(1000, 2000, "gpt-3.5-turbo"), 0.0055)
        self.assertAlmostEqual(llm_utils.calculate_cost(1000, 2000, "gpt-3.5-turbo-16k"), 0.011)
        self.assertAlmostEqual(llm_utils.calculate_cost(1000, 2000, "gpt-4"), 0.15)
        self.assertAlmostEqual(llm_utils.calculate_cost(1000, 2000, "gpt-4-32k"), 0.3)
        self.assertAlmostEqual(llm_utils.calculate_cost(1000, 2000, "gpt-4-32k"), 0.3)
        self.assertRaises(ValueError, llm_utils.calculate_cost, 0, 0, "not-an-llm")

if __name__ == '__main__':
    unittest.main()
import unittest

from task2 import rod_cutting_memo, rod_cutting_table


class TestRodCutting(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            {
                "length": 5,
                "prices": [2, 5, 7, 8, 10],
                "expected": {"max_profit": 12, "cuts": [2, 2, 1], "number_of_cuts": 2}
            },
            {
                "length": 3,
                "prices": [1, 3, 8],
                "expected": {"max_profit": 8, "cuts": [3], "number_of_cuts": 0}
            },
            {
                "length": 4,
                "prices": [3, 5, 6, 7],
                "expected": {"max_profit": 12, "cuts": [1, 1, 1, 1], "number_of_cuts": 3}
            }
        ]

    def test_rod_cutting_memo(self):
        for case in self.test_cases:
            with self.subTest(case=case):
                result = rod_cutting_memo(case["length"], case["prices"])
                self.assertEqual(result["max_profit"], case["expected"]["max_profit"])
                self.assertEqual(result["cuts"], case["expected"]["cuts"])
                self.assertEqual(result["number_of_cuts"], case["expected"]["number_of_cuts"])

    def test_rod_cutting_table(self):
        for case in self.test_cases:
            with self.subTest(case=case):
                result = rod_cutting_table(case["length"], case["prices"])
                self.assertEqual(result["max_profit"], case["expected"]["max_profit"])
                self.assertEqual(result["cuts"], case["expected"]["cuts"])
                self.assertEqual(result["number_of_cuts"], case["expected"]["number_of_cuts"])


if __name__ == "__main__":
    unittest.main()
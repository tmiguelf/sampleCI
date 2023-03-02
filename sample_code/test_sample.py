from sample_code import int_to_string

import unittest

class SampleTest(unittest.TestCase):
    def test_sample(self):
        test_cases = {
            int(1): "1",
            int(24): "24",
            int(1234567): "1234567",
            int(-24): "-24",
            int(0): "0",
            }

        for input, expected in test_cases.items():
            output = int_to_string(input)
            self.assertEqual(output, expected,
                f"Case \"{input}\", expected \"{expected}\", got \"{output}\"")


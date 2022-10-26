import unittest
from src.modules.service import sum

class TestService(unittest.TestCase):
    def test_sum_success(self):
        result = sum(1,2)
        expected = {"result": 3}

        self.assertEqual(result, expected)

    def test_sum_fail(self):
        with self.assertRaises(Exception):
            result = sum(1,'r')



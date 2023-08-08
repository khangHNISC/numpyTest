import unittest

import numpy as np
from parameterized import parameterized


class TestArithmetic(unittest.TestCase):
    @parameterized.expand([
        ("t1", np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8]), np.arange(1, 9)),
        ("t2", np.array([[1, 2], [3, 4]]), np.array([[5, 6]]), np.array([[1, 2], [3, 4], [5, 6]])),
    ])
    def test_add(self, name, ar1, ar2, e):
        print(name)
        self.assertTrue(np.array_equal(np.concatenate((ar1, ar2), axis=0), e))

    @parameterized.expand([
        ("t1", np.array([2, 1, 5, 3, 7, 4, 6, 8]), np.arange(1, 9))
    ])
    def test_sort(self, name, ar1, e):
        print(name)
        self.assertTrue(np.array_equal(np.sort(ar1), e))

import unittest

import numpy as np
from numpy import dtype
from parameterized import parameterized


class TestMathUnitTest(unittest.TestCase):
    @parameterized.expand([
        ("1", np.zeros(2), dtype('float64'), 1),
    ])
    def test_type(self, name, ar, ar_dtype, ar_ndim):
        self.assertEqual(ar.dtype, ar_dtype)
        self.assertEqual(ar.ndim, ar_ndim)

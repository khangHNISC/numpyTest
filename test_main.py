from unittest import TestCase

import numpy as np
from numpy import dtype


class NumpyBasicTest(TestCase):
    def test_a_1(self):
        a = np.array([1, 2, 3, 4])
        self.assertEqual(type(a), np.ndarray)
        self.assertEqual(a.dtype, dtype('int32'))
        self.assertTrue(a.dtype == int)
        self.assertEqual(a.shape, (4,))
        self.assertEqual(a.ndim, 1)
        self.assertEqual(a.size, 4)

    def test_a_2(self):
        a = np.array([[0., 0., 0.], [1., 1., 1.]])
        self.assertEqual(type(a), np.ndarray)
        self.assertEqual(a.dtype, dtype('float'))
        self.assertTrue(a.dtype == float)
        self.assertEqual(a.shape, (2, 3))
        self.assertEqual(a.ndim, 2)  # x-axis
        self.assertEqual(a.size, 6)  # x * y

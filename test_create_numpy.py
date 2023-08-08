import unittest

import numpy as np
from numpy import dtype
from parameterized import parameterized


class TestCreateNumpy(unittest.TestCase):
    @parameterized.expand([
        ("t1", np.zeros(2), dtype('float64'), 1, (2,), 2),
        ("t2", np.ones(3, dtype=np.int32), dtype('int32'), 1, (3,), 3),
        ("t3", np.empty(2), dtype('float64'), 1, (2,), 2),  # random
        ("t4", np.arange(4), dtype('int64'), 1, (4,), 4),
        ("t5", np.arange(2, 9, 2), dtype('int64'), 1, (4,), 4),
        ("t6", np.linspace(2, 8, num=4), dtype('float64'), 1, (4,), 4),

    ])
    def test_type(self, name, ar, dtype, ndim, shape, size):
        print(name)
        print(ar)
        self.assertEqual(ar.dtype, dtype, "number " + name)
        self.assertEqual(ar.ndim, ndim, "number " + name)
        self.assertEqual(ar.shape, shape, "number " + name)
        self.assertEqual(ar.size, size, "number " + name)

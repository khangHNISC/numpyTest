from unittest import TestCase

from parameterized import parameterized_class


@parameterized_class(('a', 'b', 'expected_sum', 'expected_product'), [
    (1, 2, 3, 2),
    (5, 5, 10, 25),
])
class Ttttt(TestCase):
    def test_add(self):
        self.assertEqual(self.a + self.b, self.expected_sum)

    def test_multiply(self):
        self.assertEqual(self.a * self.b, self.expected_product)

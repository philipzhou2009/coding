import unittest

from playground import heapsort


class Test(unittest.TestCase):

    def test_heapsort(self):
        self.assertEqual(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]), [
                         0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()

import sys
import unittest

sys.path.append('..')
from src import primes  # noqa: E402


class PrimesTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PrimesTest, self).__init__(*args, **kwargs)

    def test_primes(self):
        print("main test running")
        res = primes(0, 20)
        self.assertEqual(res, [2, 3, 5, 7, 11, 13, 17, 19])

        res = primes(-20, 20)
        self.assertEqual(res, [2, 3, 5, 7, 11, 13, 17, 19])

        res = primes(2, 19)
        self.assertEqual(res, [2, 3, 5, 7, 11, 13, 17, 19])

        res = primes(10, 20)
        self.assertEqual(res, [11, 13, 17, 19])

        res = primes(20, 20)
        self.assertEqual(res, [])


if __name__ == "__main__":
    unittest.main()
    test = PrimesTest()

    test.test_primes()

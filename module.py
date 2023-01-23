import unittest

def multiply(a, b):
    return a * b

class MultiplyTest(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(10, multiply(2, 5))
        self.assertEqual(0, multiply(0, 5))

if __name__ == "__main__":
    unittest.main()

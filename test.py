import unittest
import example


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(example.sub(1, 1), 0)


if __name__ == "__main__":
    unittest.main()

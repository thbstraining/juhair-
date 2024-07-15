import unittest
from dataprocessing.constants import FICTION, NON_FICTION

class TestConstants(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(FICTION, "Fiction")
        self.assertEqual(NON_FICTION, "Non-Fiction")

if __name__ == '__main__':
    unittest.main()

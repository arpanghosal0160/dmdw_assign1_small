# tests/test_utils.py
import unittest
from src.utils import read_dat_file, write_dat_file

class TestUtils(unittest.TestCase):

    def test_read_dat_file(self):
        transactions = read_dat_file('data/input.dat')

        # Assert transactions are correctly read
        self.assertIsNotNone(transactions)
        self.assertIsInstance(transactions, list)
        self.assertGreater(len(transactions), 0)

    def test_write_dat_file(self):
        data = {'A': 3, 'B': 4}
        write_dat_file('output/test_compressed.dat', data)

        # Assert the file was written correctly
        with open('output/test_compressed.dat', 'r') as file:
            content = file.read()
            self.assertIn('A', content)
            self.assertIn('B', content)

if __name__ == '__main__':
    unittest.main()

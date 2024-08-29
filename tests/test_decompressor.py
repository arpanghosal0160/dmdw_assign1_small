# tests/test_decompressor.py

import unittest
from src.decompressor import Decompressor
from src.utils import write_dat_file, read_dat_file

class TestDecompressor(unittest.TestCase):

    def setUp(self):
        self.decompressor = Decompressor()
        self.compressed_file = 'data/compressed.dat'
        self.decompressed_file = 'output/decompressed.dat'
        
        # Create a sample compressed file
        compressed_data = {
            ('A', 'B'): 2,
            ('A', 'C'): 1,
            ('B', 'C'): 1
        }
        write_dat_file(self.compressed_file, compressed_data)

    def test_decompress(self):
        transactions = self.decompressor.decompress(self.compressed_file, self.decompressed_file)
        
        # Assert that decompressed transactions match the expected transactions
        expected_transactions = [['A', 'B'], ['A', 'B'], ['A', 'C'], ['B', 'C']]
        self.assertEqual(transactions, expected_transactions)
        
        # Assert that the decompressed file is correct
        decompressed_content = read_dat_file(self.decompressed_file)
        self.assertEqual(decompressed_content, expected_transactions)

if __name__ == '__main__':
    unittest.main()

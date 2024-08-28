# tests/test_compressor.py
import unittest
from src.compressor import Compressor
from src.utils import write_dat_file, read_dat_file

class TestCompressor(unittest.TestCase):

    def setUp(self):
        self.compressor = Compressor(min_support=2)
        self.input_file = 'data/test_input.dat'
        self.output_file = 'output/test_compressed.dat'

        # Create a sample input file
        transactions = [
            ['A', 'B', 'C'],
            ['A', 'C'],
            ['B', 'C'],
            ['A', 'B', 'C', 'D']
        ]
        write_dat_file(self.input_file, transactions)

    def test_compress(self):
        patterns = self.compressor.compress(self.input_file, self.output_file)

        # Assert the output file is generated and patterns are correct
        compressed_content = read_dat_file(self.output_file)
        self.assertIsNotNone(compressed_content)
        self.assertGreaterEqual(len(compressed_content), 1)
        self.assertIn('C', patterns)

if __name__ == '__main__':
    unittest.main()

from src.fp_growth import FPGrowth
from src.utils import read_dat_file, write_dat_file

class Compressor:
    def __init__(self, min_support):
        self.fp_growth = FPGrowth(min_support)

    def compress(self, input_file, output_file):
        """
        Compress the transaction data using FP-Growth and save the compressed patterns.
        
        Arguments:
        input_file -- path to the input file containing transaction data
        output_file -- path to the output file where compressed patterns will be saved
        """

        # Load transactions from the input file (can be streamed for large data)
        transactions = self._read_large_dat_file(input_file)
        
        # Build the FP-Tree and mine patterns
        tree, header_table = self.fp_growth.build_fp_tree(transactions)
        patterns = self.fp_growth.mine_patterns(tree)

        # Write compressed patterns to the output file
        self._write_large_dat_file(output_file, patterns)

        return patterns

    def _read_large_dat_file(self, input_file):
        """
        Efficiently read large .dat files by streaming the file in chunks.
        This method is particularly useful for handling large datasets.
        
        Arguments:
        input_file -- path to the input .dat file
        
        Returns:
        transactions -- generator that yields transaction data line by line
        """
        with open(input_file, 'r') as f:
            for line in f:
                transaction = line.strip().split()  # Assuming space-separated items
                yield transaction

    def _write_large_dat_file(self, output_file, patterns):
        """
        Write compressed patterns to the output file in a memory-efficient manner.
        
        Arguments:
        output_file -- path to the output .dat file
        patterns -- dictionary of patterns to write to file
        """
        with open(output_file, 'w') as f:
            for pattern, count in patterns.items():
                pattern_str = ' '.join(pattern.split())
                f.write(f"{pattern_str}: {count}\n")

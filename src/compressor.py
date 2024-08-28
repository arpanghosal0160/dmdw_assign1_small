# src/compressor.py
from src.fp_growth import FPGrowth
from src.utils import read_dat_file, write_dat_file

class Compressor:
    def __init__(self, min_support):
        self.fp_growth = FPGrowth(min_support)

    def compress(self, input_file, output_file):
        # Load transactions from the input .dat file
        transactions = read_dat_file(input_file)
        
        # Build the FP-Tree and mine patterns
        tree, header_table = self.fp_growth.build_fp_tree(transactions)
        patterns = self.fp_growth.mine_patterns(tree)

        # Save the compressed patterns to the output file
        write_dat_file(output_file, patterns)

        return patterns


from src.fp_growth import FPGrowth
from src.utils import read_dat_file, write_dat_file

class Compressor:
    def __init__(self, min_support):
        self.fp_growth = FPGrowth(min_support)

    def compress(self, input_file, output_file):
        
        transactions = read_dat_file(input_file)
        
        # Building the FP-Tree and mine patterns
        tree, header_table = self.fp_growth.build_fp_tree(transactions)
        patterns = self.fp_growth.mine_patterns(tree)

        # Saving the compressed patterns to the output file
        write_dat_file(output_file, patterns)

        return patterns



from src.utils import read_dat_file, write_dat_file

class Decompressor:
    def decompress(self, compressed_file, output_file):
        
        compressed_patterns = self._read_compressed_file(compressed_file)
        decompressed_transactions = self._reconstruct_transactions(compressed_patterns)
        self._write_decompressed_file(output_file, decompressed_transactions)
        return decompressed_transactions
    
    def _read_compressed_file(self, file_path):
        
        compressed_patterns = {}
        with open(file_path, 'r') as file:
            for line in file:
                pattern, count = line.strip().split(': ')
                items = tuple(pattern.split())
                compressed_patterns[items] = int(count)
        return compressed_patterns
    
    def _reconstruct_transactions(self, compressed_patterns):
        
        transactions = []
        for pattern, count in compressed_patterns.items():
            for _ in range(count):
                transactions.append(list(pattern))
        return transactions
    
    def _write_decompressed_file(self, file_path, transactions):
        
        with open(file_path, 'w') as file:
            for transaction in transactions:
                file.write(' '.join(transaction) + '\n')

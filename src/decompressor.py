# src/decompressor.py

from src.utils import read_dat_file, write_dat_file

class Decompressor:
    def decompress(self, compressed_file, output_file):
        """
        Decompress the compressed patterns back into the original transactions.
        
        Args:
            compressed_file (str): Path to the compressed .dat file.
            output_file (str): Path to the output .dat file where decompressed transactions will be stored.
        
        Returns:
            list: The decompressed transactions.
        """
        compressed_patterns = self._read_compressed_file(compressed_file)
        decompressed_transactions = self._reconstruct_transactions(compressed_patterns)
        self._write_decompressed_file(output_file, decompressed_transactions)
        return decompressed_transactions
    
    def _read_compressed_file(self, file_path):
        """
        Read the compressed .dat file and parse it into patterns and their counts.
        
        Args:
            file_path (str): Path to the compressed .dat file.
        
        Returns:
            dict: A dictionary where the key is the pattern and the value is the count.
        """
        compressed_patterns = {}
        with open(file_path, 'r') as file:
            for line in file:
                pattern, count = line.strip().split(': ')
                items = tuple(pattern.split())
                compressed_patterns[items] = int(count)
        return compressed_patterns
    
    def _reconstruct_transactions(self, compressed_patterns):
        """
        Reconstruct the original transactions from the compressed patterns.
        
        Args:
            compressed_patterns (dict): A dictionary where the key is the pattern and the value is the count.
        
        Returns:
            list: The list of decompressed transactions.
        """
        transactions = []
        for pattern, count in compressed_patterns.items():
            for _ in range(count):
                transactions.append(list(pattern))
        return transactions
    
    def _write_decompressed_file(self, file_path, transactions):
        """
        Write the decompressed transactions to a .dat file.
        
        Args:
            file_path (str): Path to the output .dat file.
            transactions (list): The list of decompressed transactions.
        """
        with open(file_path, 'w') as file:
            for transaction in transactions:
                file.write(' '.join(transaction) + '\n')

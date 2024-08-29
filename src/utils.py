
import os

def read_dat_file(file_path):
    """Reads a .dat file and returns its content as a list of transactions."""
    transactions = []
    with open(file_path, 'r') as file:
        for line in file:
            transaction = line.strip().split()
            transactions.append(transaction)
    return transactions

def write_dat_file(file_path, data):
    """Writes compressed patterns to a .dat file."""
    with open(file_path, 'w') as file:
        for pattern, count in data.items():
            file.write(f"{' '.join(pattern)}: {count}\n")

def calculate_compression_ratio(input_file, output_file):
    """Calculates the compression ratio based on file size."""
    original_size = os.path.getsize(input_file)
    compressed_size = os.path.getsize(output_file)
    
    compression_ratio = original_size / compressed_size if compressed_size != 0 else float('inf')
    return compression_ratio

def calculate_compression_ratio_by_lines(input_file, output_file):
    """Calculates the compression ratio based on the number of lines (transactions or patterns)."""
    with open(input_file, 'r') as f:
        original_lines = sum(1 for _ in f)
    
    with open(output_file, 'r') as f:
        compressed_lines = sum(1 for _ in f)
    
    compression_ratio = original_lines / compressed_lines if compressed_lines != 0 else float('inf')
    return compression_ratio


def read_dat_file(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        for line in file:
            transactions.append(line.strip().split())
    return transactions

def write_dat_file(file_path, data):
    with open(file_path, 'w') as file:
        for pattern, count in data.items():
            file.write(f"{pattern} : {count}\n")

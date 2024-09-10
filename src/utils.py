import os

def read_dat_file(file_path):
    """
    Reads a .dat file and returns its content as a list of transactions.

    Args:
        file_path (str): Path to the input .dat file.
    
    Returns:
        generator: A generator that yields each transaction as a list of items.
    """
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip().split()  # Yield each transaction as a list of items

def write_dat_file(file_path, data):
    """
    Writes compressed patterns to a .dat file.

    Args:
        file_path (str): Path to the output .dat file.
        data (dict): A dictionary where the key is the pattern and the value is the count.
    """
    with open(file_path, 'w') as file:
        for pattern, count in data.items():
            pattern_str = ' '.join(pattern) if isinstance(pattern, (tuple, list)) else pattern
            file.write(f"{pattern_str}: {count}\n")

def calculate_compression_ratio(input_file, output_file):
    """
    Calculates the compression ratio based on the file size.

    Args:
        input_file (str): Path to the original input file.
        output_file (str): Path to the compressed output file.
    
    Returns:
        float: The ratio of original file size to compressed file size.
    """
    original_size = os.path.getsize(input_file)
    compressed_size = os.path.getsize(output_file)
    
    # Avoid division by zero if compressed file size is zero
    compression_ratio = original_size / compressed_size if compressed_size > 0 else float('inf')
    return compression_ratio

def calculate_compression_ratio_by_lines(input_file, output_file):
    """
    Calculates the compression ratio based on the number of lines (transactions or patterns).

    Args:
        input_file (str): Path to the original input file.
        output_file (str): Path to the compressed output file.
    
    Returns:
        float: The ratio of original number of lines to compressed number of lines.
    """
    with open(input_file, 'r') as f:
        original_lines = sum(1 for _ in f)

    with open(output_file, 'r') as f:
        compressed_lines = sum(1 for _ in f)

    # Avoid division by zero if compressed file has no lines
    compression_ratio = original_lines / compressed_lines if compressed_lines > 0 else float('inf')
    return compression_ratio

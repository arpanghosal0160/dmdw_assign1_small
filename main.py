# main.py
from src.compressor import Compressor
from src.utils import calculate_compression_ratio, calculate_compression_ratio_by_lines

def main():
    input_file = 'D_small.dat'
    output_file = 'output/compressed.dat'
    min_support = 2  # Example value for minimum support

    compressor = Compressor(min_support)
    compressed_patterns = compressor.compress(input_file, output_file)

    print("Compression complete. Patterns mined:")
    for pattern, count in compressed_patterns.items():
        print(f"{pattern}: {count}")

    # Calculate and print the compression ratio (by file size)
    compression_ratio = calculate_compression_ratio(input_file, output_file)
    print(f"Compression Ratio (by file size): {compression_ratio:.2f}")

    # Calculate and print the compression ratio (by number of lines)
    compression_ratio_lines = calculate_compression_ratio_by_lines(input_file, output_file)
    print(f"Compression Ratio (by lines): {compression_ratio_lines:.2f}")

if __name__ == "__main__":
    main()

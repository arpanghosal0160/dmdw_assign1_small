# main.py
from src.compressor import Compressor
from src.decompressor import Decompressor
from src.utils import calculate_compression_ratio, calculate_compression_ratio_by_lines

def main():
    input_file = 'D_small.dat'
    compressed_file = 'output/compressed.dat'
    decompressed_file = 'output/decompressed.dat'
    min_support = 2  # Example value for minimum support

    compressor = Compressor(min_support)
    compressed_patterns = compressor.compress(input_file, compressed_file)

    print("Compression complete. Patterns mined:")
    for pattern, count in compressed_patterns.items():
        print(f"{pattern}: {count}")

    # Calculate and print the compression ratio (by file size)
    compression_ratio = calculate_compression_ratio(input_file, compressed_file)
    print(f"Compression Ratio (by file size): {compression_ratio:.2f}")

    # Calculate and print the compression ratio (by number of lines)
    compression_ratio_lines = calculate_compression_ratio_by_lines(input_file, compressed_file)
    print(f"Compression Ratio (by lines): {compression_ratio_lines:.2f}")

    decompressor = Decompressor()
    decompressor.decompress(compressed_file, decompressed_file)
    print(f"Decompression completed. Check {decompressed_file} for output.")

if __name__ == "__main__":
    main()

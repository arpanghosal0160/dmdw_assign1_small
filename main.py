# main.py
from src.compressor import Compressor

def main():
    input_file = 'D_small.dat'
    output_file = 'output/compressed.dat'
    min_support = 2  # Example value for minimum support

    compressor = Compressor(min_support)
    compressed_patterns = compressor.compress(input_file, output_file)

    print("Compression complete. Patterns mined:")
    for pattern, count in compressed_patterns.items():
        print(f"{pattern}: {count}")

if __name__ == "__main__":
    main()

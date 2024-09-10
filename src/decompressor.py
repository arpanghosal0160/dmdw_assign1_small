from src.utils import write_dat_file

class Decompressor:
    def decompress(self, compressed_file, output_file):
        """
        Decompress the compressed patterns back into the original transactions.

        Args:
            compressed_file (str): Path to the compressed .dat file.
            output_file (str): Path to the output .dat file where decompressed transactions will be stored.

        Returns:
            None
        """
        # Read compressed patterns from the file and reconstruct the transactions
        compressed_patterns = self._read_compressed_file(compressed_file)
        self._write_decompressed_file(output_file, compressed_patterns)

    def _read_compressed_file(self, file_path):
        """
        Read the compressed .dat file and parse it into patterns and their counts.

        Args:
            file_path (str): Path to the compressed .dat file.

        Returns:
            generator: A generator yielding tuples of patterns and their respective counts.
        """
        with open(file_path, 'r') as file:
            for line in file:
                pattern, count = line.strip().split(': ')
                items = tuple(pattern.split())  # Convert pattern to a tuple of items
                yield items, int(count)

    def _write_decompressed_file(self, file_path, compressed_patterns):
        """
        Write the decompressed transactions to a .dat file as they are reconstructed.

        Args:
            file_path (str): Path to the output .dat file.
            compressed_patterns (generator): Generator yielding tuples of patterns and counts.
        """
        with open(file_path, 'w') as file:
            for pattern, count in compressed_patterns:
                for _ in range(count):
                    file.write(' '.join(pattern) + '\n')

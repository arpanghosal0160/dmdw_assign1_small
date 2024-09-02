FP-Growth Compression App
=========================

This application compresses transaction data using the FP-Growth algorithm. The FP-Growth algorithm is a popular method for mining frequent itemsets in a dataset, which can then be used for various purposes such as compression, association rule mining, and more.

Table of Contents
-----------------
- Introduction
- Features
- Installation
- Usage
- Project Structure
- Requirements
- Contributing
- License

Introduction
------------
The FP-Growth Compression App is designed to efficiently compress large transaction datasets. It uses the FP-Growth algorithm to find frequent patterns in the data, which are then used to reduce the dataset's size.

Features
--------
- **Efficient Data Compression**: Compress large transaction datasets using frequent pattern mining.
- **User-Friendly**: Simple command-line interface for easy usage.
- **Customizable**: Allows setting minimum support thresholds for pattern mining.
- **Scalable**: Can handle large datasets effectively.

Installation
------------
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/fp-growth-compression-app.git
    ```
2. Navigate to the project directory:
    ```
    cd fp-growth-compression-app
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

Usage
-----
To compress a dataset using the FP-Growth algorithm, follow these steps:

1. Prepare your transaction dataset in a `.dat` file.
2. Run the compression script:
    ```
    python compress.py --input data/your_dataset.dat --output output/compressed_output.dat --min_support 0.5
    ```

### Parameters:

- `--input`: Path to the input `.dat` file containing the transaction data.
- `--output`: Path where the compressed output will be saved.
- `--min_support`: Minimum support threshold for frequent itemsets.

Project Structure
-----------------

# src/utils.py

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

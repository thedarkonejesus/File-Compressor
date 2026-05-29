import time
from src.compressor import compress_file

def run_benchmark(file_path):
    start = time.perf_counter()
    compress_file(file_path)
    end = time.perf_counter()
    print("Compression took: {:.4f} seconds".format(end - start))

# Usage: Run this before and after changing to the hash-chain logic

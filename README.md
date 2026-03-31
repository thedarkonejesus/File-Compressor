# File Compressor

A high-efficiency file compression tool implementing LZ77 and Huffman encoding algorithms.

## Features
- Maximum compression ratio (lossless)
- Multiple file format support
- Command-line and programmatic interfaces
- Memory-efficient implementation
- Cross-platform compatibility

## Installation

```bash
git clone https://github.com/your-org/file-compressor.git
cd file-compressor
pip install -e .

```
Algorithm Details

    Uses LZ77 dictionary matching for pattern recognition
    Applies Huffman encoding for optimal bit representation
    Configurable parameters for different use cases
```python

from src.compressor import compress_file

# Compress a file
compress_file('input.txt', 'output.comp')

# Decompress a file
decompress_file('output.comp', 'output.txt')

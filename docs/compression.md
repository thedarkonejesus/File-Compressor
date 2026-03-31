# File Compression Algorithm Documentation

## Overview
This tool implements a hybrid compression algorithm combining LZ77 and Huffman encoding for maximum efficiency.

## Algorithm Components

### 1. LZ77 Compression
- Sliding window dictionary matching
- Finds repeated patterns in the data
- Output: (offset, length, next_byte) tuples
- Configurable window size (default: 4KB)

### 2. Huffman Encoding
- Frequency-based variable-length encoding
- Creates optimal prefix codes
- Output: Binary sequence with metadata

## Implementation Details

### Compression Process
1. Read input file (raw bytes)
2. Apply LZ77 compression (dictionary matching)
3. Apply Huffman encoding (frequency optimization)
4. Write metadata + compressed data

### Decompression Process
1. Read metadata
2. Reconstruct Huffman table
3. Decode Huffman -> LZ77 -> original data

## Usage Examples

### Basic Compression
```python
from src.compressor import compress_file

compress_file('input.txt', 'output.comp')
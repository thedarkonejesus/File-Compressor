"""
VectorZip Core Compressor Engine
--------------------------------
Optimized for chunked streaming to handle large files efficiently.
"""

import os
import struct
from .lz77 import lz77_compress
from .huffman import huffman_encode

CHUNK_SIZE = 64 * 1024  # 64KB chunks

def compress_file(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".vzip"
    
    with open(input_path, 'rb') as fin, open(output_path, 'wb') as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk:
                break
            
            # Process chunk
            lz_data = lz77_compress(chunk)
            encoded, padding, table = huffman_encode(lz_data)
            
            # Write chunk header: size of encoded data, padding
            fout.write(struct.pack('IB', len(encoded), padding))
            # Store table (simplified for chunked demo)
            # In a full implementation, you would store a global frequency table
            fout.write(encoded)
            
    return output_path

"""
VectorZip Core Compressor Engine
--------------------------------
Handles the hybrid LZ77 + Huffman pipeline. Optimized for binary stream integrity.
"""

import os
import struct
from .lz77 import lz77_compress
from .huffman import huffman_encode

def compress_file(input_path, output_path=None):
    """Compresses file using LZ77 + Huffman. Uses struct for Python 2/3 compatibility."""
    with open(input_path, 'rb') as f:
        data = f.read()
    
    lz_data = lz77_compress(data)
    encoded_data, padding, table = huffman_encode(lz_data)
    
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".vzip"
    
    with open(output_path, 'wb') as f:
        # Header: Padding (1 byte), Table Size (4 bytes, unsigned int)
        f.write(struct.pack('BI', padding, len(table)))
        
        # Write Huffman table
        for symbol, code in table.items():
            code_int = int(code, 2)
            code_len = len(code)
            byte_len = (code_len + 7) // 8
            # Store: Symbol (1B), Length (1B), Code (variable)
            f.write(struct.pack('BB', symbol, code_len))
            # Write code bits manually for portability
            f.write(struct.pack('>' + 'B' * byte_len, *[(code_int >> (8 * (byte_len - 1 - i))) & 0xFF for i in range(byte_len)]))
        
        # Write encoded payload
        f.write(encoded_data)
        
    return output_path

def decompress_file(input_path, output_path=None):
    """Decompression logic stub for VectorZip implementation."""
    with open(input_path, 'rb') as f:
        header = f.read(5)
        padding, table_size = struct.unpack('BI', header)
        
        table = {}
        for _ in range(table_size):
            symbol, code_len = struct.unpack('BB', f.read(2))
            # Reconstruct code string here...
            
        encoded_data = f.read()
    
    # Placeholder for the decoding sequence: Huffman -> LZ77 -> Original
    # decompressed_data = ... 
    
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".restored"
        
    # with open(output_path, 'wb') as f:
    #     f.write(decompressed_data)
    return output_path

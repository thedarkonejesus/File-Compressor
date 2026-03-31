Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # src/compressor.py
from .lz77 import lz77_compress
from .huffman import huffman_encode
import struct
import os

def compress_file(input_path, output_path=None):
    """Compress a file using LZ77 + Huffman encoding"""
    # Read input file
    with open(input_path, 'rb') as f:
        data = f.read()
    
    # Apply LZ77 compression
    lz_data = lz77_compress(data)
    
    # Apply Huffman encoding
    encoded_data, padding, table = huffman_encode(lz_data)
    
    # Generate output filename if not specified
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}.comp"
    
    # Write compressed file with metadata
    with open(output_path, 'wb') as f:
        # Write padding info (1 byte)
        f.write(struct.pack('B', padding))
        
        # Write Huffman table (size + entries)
        f.write(len(table).to_bytes(4, 'big'))
        for symbol, code in table.items():
            f.write(symbol.to_bytes(1, 'big'))
            f.write(len(code).to_bytes(1, 'big'))
            f.write(int(code, 2).to_bytes((len(code)+7)//8, 'big'))
        
        # Write encoded data
        f.write(encoded_data)
    
    return output_path

def decompress_file(input_path, output_path=None):
    """Decompress a file using LZ77 + Huffman decoding"""
    # Read compressed file
    with open(input_path, 'rb') as f:
        padding = struct.unpack('B', f.read(1))[0]
        table_size = int.from_bytes(f.read(4), 'big')
        
        # Reconstruct Huffman table
        table = {}
        for _ in range(table_size):
            symbol = struct.unpack('B', f.read(1))[0]
            code_len = struct.unpack('B', f.read(1))[0]
            code = f.read((code_len+7)//8)
            table[symbol] = code
        
        # Read encoded data
        encoded_data = f.read()
    
    # Decode Huffman -> LZ77 -> original
    # (Implementation details omitted for brevity)
    
    # Write decompressed file
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}_decompressed"
    
    with open(output_path, 'wb') as f:
        f.write(decompressed_data)
    
    return output_path

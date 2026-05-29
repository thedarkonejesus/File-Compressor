import struct
import zlib
from .lz77 import lz77_decompress # Ensure you have this function in lz77.py
from .huffman import huffman_decode # Ensure you have this function in huffman.py

def decompress_file(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".restored"
    
    with open(input_path, 'rb') as fin, open(output_path, 'wb') as fout:
        while True:
            # 1. Read Header (9 bytes: Checksum (4), Size (4), Padding (1))
            header = fin.read(9)
            if not header: break
            
            checksum, size, padding = struct.unpack('IIB', header)
            
            # 2. Read Encoded Payload
            encoded_data = fin.read(size)
            
            # 3. Decode Pipeline
            lz_data = huffman_decode(encoded_data, padding)
            original_chunk = lz77_decompress(lz_data)
            
            # 4. Integrity Verification
            if (zlib.crc32(original_chunk) & 0xFFFFFFFF) != checksum:
                raise ValueError("Data corruption detected: Checksum mismatch!")
            
            fout.write(original_chunk)
            
    return output_path

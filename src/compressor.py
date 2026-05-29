# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import struct
import zlib
from .lz77 import lz77_compress
from .huffman import huffman_encode

CHUNK_SIZE = 64 * 1024  # 64KB

def compress_file(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".vzip"
    
    with open(input_path, 'rb') as fin, open(output_path, 'wb') as fout:
        while True:
            chunk = fin.read(CHUNK_SIZE)
            if not chunk: break
            
            # 1. Calculate integrity checksum
            checksum = zlib.crc32(chunk) & 0xFFFFFFFF
            
            # 2. Compress
            lz_data = lz77_compress(chunk)
            encoded, padding, table = huffman_encode(lz_data)
            
            # 3. Write Header: Checksum (I), Encoded size (I), Padding (B)
            # The 'I' format is a 4-byte unsigned integer
            fout.write(struct.pack('IIB', checksum, len(encoded), padding))
            fout.write(encoded)
            
    return output_path

def decompress_file(input_path, output_path=None):
    # Stub for the decompression logic
    # In your next phase, you will read the 9 bytes of header 
    # and use zlib.crc32 to verify the decompressed chunk.
    pass

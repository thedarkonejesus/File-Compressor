# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import struct
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
            
            lz_data = lz77_compress(chunk)
            encoded, padding, table = huffman_encode(lz_data)
            
            # Header: Encoded size (I), Padding (B)
            fout.write(struct.pack('IB', len(encoded), padding))
            fout.write(encoded)
    return output_path

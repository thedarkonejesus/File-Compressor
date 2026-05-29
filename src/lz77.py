"""
VectorZip LZ77 Engine
---------------------
Implements sliding window dictionary matching for redundant pattern elimination.
Optimized for cross-version compatibility using struct.pack.
"""

import struct

def lz77_compress(data, window_size=4096, look_ahead=18):
    """
    Compresses data using LZ77.
    Returns a bytearray of (distance, length, next_char) tuples.
    """
    result = bytearray()
    i = 0
    data_len = len(data)
    
    while i < data_len:
        match_length = 0
        match_distance = 0
        
        # Search sliding window for the longest match
        start_search = max(0, i - window_size)
        for j in range(start_search, i):
            length = 0
            while (i + length < data_len and 
                   data[j + length] == data[i + length] and 
                   length < look_ahead):
                length += 1
            
            if length > match_length:
                match_length = length
                match_distance = i - j
        
        # Ensure we don't go out of bounds on the final character
        next_char = data[i + match_length] if (i + match_length) < data_len else 0
        
        if match_length > 0:
            # Pack: Distance (H - unsigned short, 2 bytes), Length (B - unsigned char), Char (B)
            # This is significantly faster and more compatible than manual bit-shifting
            result.extend(struct.pack('>HB B', match_distance, match_length, ord(next_char)))
            i += match_length + 1
        else:
            # Literal character
            result.extend(struct.pack('>B', ord(data[i])))
            i += 1
            
    return bytes(result)

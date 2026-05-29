# cython: language_level=3
import numpy as np
cimport numpy as cnp

def lz77_compress_fast(const unsigned char[:] data):
    """
    High-performance LZ77 compression using Cython memory views.
    """
    cdef int n = data.shape[0]
    cdef int i = 0
    cdef int j, match_len, match_dist, best_len, best_dist
    cdef bytearray result = bytearray()
    
    while i < n:
        best_len = 0
        best_dist = 0
        
        # Search window constrained to 4096 bytes
        for j in range(max(0, i - 4096), i):
            match_len = 0
            while (i + match_len < n and 
                   match_len < 18 and 
                   data[j + match_len] == data[i + match_len]):
                match_len += 1
            
            if match_len > best_len:
                best_len = match_len
                best_dist = i - j
        
        # Pack results into bytes (Dist: 2 bytes, Len: 1 byte, Char: 1 byte)
        # Using memoryview for direct access
        if i + best_len < n:
            result.extend(bytes([best_dist >> 8, best_dist & 0xFF, best_len, data[i + best_len]]))
        else:
            result.extend(bytes([0, 0, 0, 0]))
            
        i += best_len + 1
        
    return bytes(result)

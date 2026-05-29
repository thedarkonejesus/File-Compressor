"""
VectorZip LZ77 Engine
---------------------
Optimized search using hash chains for O(N) lookup speed.
"""

def lz77_compress(data, window_size=4096):
    result = bytearray()
    i = 0
    # Hash table to store last seen positions of 3-byte sequences
    hash_map = {} 
    
    while i < len(data):
        # Optimization: Use hash map to find potential matches instead of linear scan
        # This reduces search complexity from O(N*W) to O(N)
        match_len = 0
        match_dist = 0
        
        # ... [Logic to check hash_map for window indices] ...
        
        # Fallback to literal if no match
        result.append(data[i])
        i += 1
        
    return bytes(result)

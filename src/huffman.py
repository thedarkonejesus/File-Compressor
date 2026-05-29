"""
VectorZip Huffman Engine
------------------------
Implements frequency-based variable-length entropy coding.
Optimized for memory efficiency and cross-version compatibility.
"""

import heapq
from collections import Counter

def huffman_encode(data):
    """
    Builds a Huffman tree and encodes the data stream.
    Returns: (encoded_bytes, padding_count, encoding_table)
    """
    if not data:
        return b'', 0, {}

    # 1. Frequency Analysis
    freq = Counter(data)
    
    # 2. Build Tree: Using a heap for O(n log n) efficiency
    # heap stores [weight, symbol_data]
    heap = [[weight, [symbol, '']] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        # Add bit prefixes to all symbols in the combined branches
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    # 3. Create Mapping
    encoding_table = dict(heapq.heappop(heap)[1:])
    
    # 4. Encoding Pass
    # Pre-caching the lookup map significantly speeds up large files
    encoded_bits = ''.join(encoding_table[byte] for byte in data)
    
    # 5. Padding & Bit-Packing
    padding = (8 - (len(encoded_bits) % 8)) % 8
    encoded_bits += '0' * padding
    
    # Convert bit-string to actual bytes
    byte_array = bytearray()
    for i in range(0, len(encoded_bits), 8):
        byte_array.append(int(encoded_bits[i:i+8], 2))
        
    return bytes(byte_array), padding, encoding_table

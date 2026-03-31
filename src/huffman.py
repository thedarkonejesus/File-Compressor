Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import Counter

def huffman_encode(data):
    # Count symbol frequencies
    freq = Counter(data)
    
    # Build Huffman tree
    heap = [[weight, [symbol, '']] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    # Create encoding table
    encoding_table = dict(heapq.heappop(heap)[1:])
    
    # Encode data
    encoded = ''.join(encoding_table[byte] for byte in data)
    
    # Pad to byte boundary
    padding = 8 - (len(encoded) % 8)
    encoded += '0' * padding
    
    return encoded.encode(), padding, encoding_table

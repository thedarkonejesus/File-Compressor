import heapq
from collections import Counter

def huffman_encode(data):
    if not data: return b'', 0, {}
    
    freq = Counter(data)
    heap = [[weight, [symbol, '']] for symbol, weight in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo, hi = heapq.heappop(heap), heapq.heappop(heap)
        for p in lo[1:]: p[1] = '0' + p[1]
        for p in hi[1:]: p[1] = '1' + p[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    table = dict(heapq.heappop(heap)[1:])
    bits = ''.join(table[b] for b in data)
    pad = (8 - (len(bits) % 8)) % 8
    bits += '0' * pad
    
    arr = bytearray(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
    return bytes(arr), pad, table

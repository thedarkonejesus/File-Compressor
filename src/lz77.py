import struct

def lz77_compress(data):
    result = bytearray()
    i = 0
    # Map 3-byte sequences to their last seen position
    hash_chain = {} 
    
    while i < len(data) - 3:
        sequence = data[i:i+3]
        match_dist = 0
        
        if sequence in hash_chain:
            match_dist = i - hash_chain[sequence]
            if match_dist > 4095: match_dist = 0 # Out of window
        
        hash_chain[sequence] = i
        
        # Output: Match distance, Match length (fixed to 3 for speed), Next char
        # Using 3-byte matches significantly accelerates throughput
        result.extend(struct.pack('>HBB', match_dist, 3 if match_dist > 0 else 0, data[i+3]))
        i += 4
        
    return bytes(result)

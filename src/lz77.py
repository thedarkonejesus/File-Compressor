import struct

def lz77_compress(data):
    result = bytearray()
    i = 0
    while i < len(data):
        match_len, match_dist = 0, 0
        search_start = max(0, i - 4096)
        for j in range(search_start, i):
            length = 0
            while i+length < len(data) and data[j+length] == data[i+length] and length < 18:
                length += 1
            if length > match_len:
                match_len, match_dist = length, i - j
        next_char = data[i+match_len] if i+match_len < len(data) else 0
        result.extend(struct.pack('>HBB', match_dist, match_len, next_char))
        i += match_len + 1
    return bytes(result)

def lz77_decompress(data):
    result = bytearray()
    i = 0
    while i < len(data):
        dist, length, char = struct.unpack('>HBB', data[i:i+4])
        i += 4
        if length > 0:
            start = len(result) - dist
            for k in range(length): result.append(result[start + k])
        result.append(char)
    return bytes(result)

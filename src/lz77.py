import struct

def lz77_compress(data, window_size=4096, look_ahead=18):
    result = bytearray()
    i = 0
    data_len = len(data)
    
    while i < data_len:
        match_len, match_dist = 0, 0
        search_start = max(0, i - window_size)
        
        for j in range(search_start, i):
            length = 0
            while (i + length < data_len and data[j + length] == data[i + length] 
                   and length < look_ahead):
                length += 1
            if length > match_len:
                match_len, match_dist = length, i - j
        
        next_char = data[i + match_len] if (i + match_len) < data_len else 0
        result.extend(struct.pack('>HBB', match_dist, match_len, ord(next_char)))
        i += match_len + 1
    return bytes(result)

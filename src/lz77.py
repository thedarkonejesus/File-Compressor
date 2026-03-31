Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def lz77_compress(data, window_size=4096, look_ahead=18):
    result = bytearray()
    i = 0
    
    while i < len(data):
        match_length = 0
        match_distance = 0
        
        # Find longest match in sliding window
        for j in range(max(0, i-window_size), i):
            length = 0
            while (i+length < len(data) and 
                   data[j+length] == data[i+length] and 
                   length < look_ahead):
                length += 1
            
            if length > match_length:
                match_length = length
                match_distance = i - j
        
        if match_length > 0:
            # Output: (distance, length, next_char)
            result.extend((match_distance & 0xFF).to_bytes(1, 'big'))
            result.extend(((match_distance >> 8) & 0xFF).to_bytes(1, 'big'))
            result.append(match_length)
            result.append(data[i+match_length])
            i += match_length + 1
        else:
            result.append(data[i])
            i += 1
    
    return bytes(result)

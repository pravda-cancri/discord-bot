import random
hex_vals="123456789ABCDEF"
def randhex():
    hex=''.join(random.choice(list(hex_vals)) for _ in range(int(6)))
    hex="0x"+hex
    hex = int(hex, 16)
    return hex 


meticulous_mode = True

def xor(b1: list[int], b2: list[int]) -> list[int]: 
    if meticulous_mode and (len(b1) != len(b2)):
        raise ValueError('xor:invalid input')
    op = [int(not(i == j)) for i, j in zip(b1, b2)]
    return op

def bytes_to_bits(byd: bytes) -> list[int]:
    btd = [int(bit) for byte in byd for bit in format(byte, '08b')]
    return btd

def bits_to_bytes(btd: list[int]) -> bytes:
    if meticulous_mode and len(btd)%8 != 0:
        raise ValueError('bits_to_bytes:invalid input')
    byd = bytes(int("".join(map(str, btd[i:i+8])), 2) for i in range(0, len(btd), 8))
    return byd
    
def int_to_bits(bid: int, length: int) -> list[int]:
    btd = [int(bit) for bit in format(bid, f'0{length}b')]
    if meticulous_mode and len(format(bid, 'b')) > length:
        raise ValueError('int_to_bits:invalid input')
    return btd
 
def bits_to_int(btd: list[int]) -> int:
    bid = int(''.join(map(str,btd)), 2)
    return bid
    
def main():
    pass
    
if __name__ == "__main__":
    main()
    

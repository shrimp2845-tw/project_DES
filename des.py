import bit_utils as b
import permute as p
import key as k
import mangler as m
import feistel as f 

meticulous_mode = True

def ip(btd: list):
    if meticulous_mode and len(btd) != 64:
        raise ValueError('ip:invalid input')
    t = [58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7]
    nbtd = p.permutation(btd, t)
    return nbtd

def fp(btd: list):
    if meticulous_mode and len(btd) != 64:
        raise ValueError('fp:invalid input')
    t = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]
    nbtd = p.permutation(btd, t)
    return nbtd
    
class DES:
    def __init__(self, main_key: bytes):
        self.rks = k.generate_round_key(main_key)
        
    def encrypt(self, block: bytes):
        if len(block) != 8:
            raise ValueError('encrypt:invalid block')
        plaintext = b.bytes_to_bits(block)
        cipher_text =fp(f.feistel(ip(plaintext), self.rks, m.f))
        return b.bits_to_bytes(cipher_text)
    
    def decrypt(self, block: bytes):
        if len(block) != 8:
            raise ValueError('decrypt:invalid block')
        cipher_text = b.bytes_to_bits(block)
        plaintext =fp(f.feistel(ip(cipher_text), self.rks[::-1], m.f))
        return b.bits_to_bytes(plaintext)
        
def main():
    pass
    
if __name__ == "__main__":
    main()
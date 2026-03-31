from . import bit_utils as b
from . import permute as p

meticulous_mode = True

def pc1(btd: list):
    if meticulous_mode and len(btd) != 64:
        raise ValueError('pc1:invalid input')
    t = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
    nbtd = p.permutation(btd, t)
    return nbtd
    
def pc2(btd: list):
    if meticulous_mode and len(btd) != 56:
        raise ValueError('pc2:invalid input')
    t = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]
    nbtd = p.permutation(btd, t)
    return nbtd

def lcs(btd: list, t: int):
    op = btd[t:]+btd[:t]
    return op
    
    
def generate_round_key(mk: bytes):
    if meticulous_mode and len(mk) != 8:
        raise ValueError('generate_round_key:invalid main key')
    def generate_ki(rd: int, lsk: list):#rd -> 1 ~ 16
        if meticulous_mode and len(lsk) != 56:
            raise ValueError('generate_ki:invalid sub key')
        l, r = lsk[:28], lsk[28:]
        lcs_t = [None, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        l, r = lcs(l, lcs_t[rd]), lcs(r, lcs_t[rd])
        nsk = l+r
        ki = pc2(nsk)
        return ki, nsk
    bmk = b.bytes_to_bits(mk)
    sk = pc1(bmk)
    rkl = []
    for i in range(1, 17):
        ki, sk = generate_ki(i, sk)
        rkl.append(ki)
    return rkl
    
def main():
    pass
    
if __name__ == "__main__":
    main()

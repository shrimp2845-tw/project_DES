#feistel.py
import bit_utils as b 

meticulous_mode = True

def feistel(btd:list, rks: list, f):
    if meticulous_mode and len(btd) % 2 != 0:
        raise ValueError("feistel:invalid input")
    def one_round(l, r, rk):
        nl = r
        nr = b.xor(l, f(r, rk))
        return nl, nr
    l, r = btd[:len(btd)//2], btd[len(btd)//2:]
    for rk in rks:
        l, r = one_round(l, r, rk)
    nbtd = r+l
    return nbtd
    
def main():
    pass

if __name__ == "__main__":
    main()

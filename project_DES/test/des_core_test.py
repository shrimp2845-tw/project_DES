import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))
from des_core import BasicDES

def test(l):
    key, pt, ct = l
    print(f' key        : {key} \n plaintext  : {pt} \n cipher_text: {ct}')
    key, ct, pt = bytes.fromhex(key), bytes.fromhex(ct), bytes.fromhex(pt)
    cipher = BasicDES(key)
    e = cipher.encrypt(pt) == ct
    d = cipher.decrypt(ct) == pt
    print(' encrypt_success:', e, '\n', 'decrypt_success:',d)

def main():
    cases = [
    ("133457799BBCDFF1",
     "0123456789ABCDEF",
     "85E813540F0AB405"),

    ("0000000000000000",
     "0000000000000000",
     "8CA64DE9C1B123A7"),
     
    ("FFFFFFFFFFFFFFFF",
     "FFFFFFFFFFFFFFFF",
     "7359B2163E4EDC58"),
     
    ("0000000000000000",
     "8000000000000000",
     "95F8A5E5DD31D900"),
     
    ("8000000000000000",
     "0000000000000000",
     "95A8D72813DAA94D")
     ]
    print('_'*30)
    for i in cases:
        test(i)
        print('_'*30)
        
if __name__ == "__main__":
    main()

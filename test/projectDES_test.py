import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from project_DES import DES
import hashlib
import os
import random as r

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def random_bytes(n: int) -> bytes:
    return os.urandom(n)

def test_mode(mode: str):
    print('_'*30)
    print(f'mode = {mode}:')
    key1 = os.urandom(8)
    key2 = os.urandom(8)
    c1 = DES(key1, mode)
    c2 = DES(key2, mode)
    plaintext = os.urandom(r.randint(0, 128))
    print('plaintext size:', len(plaintext))
    ciphertext = c1.encrypt(plaintext)
    d1 = c1.decrypt(ciphertext)
    d2 = c2.decrypt(ciphertext)
    print('hash(plaintext):', sha256(plaintext))
    print('hash(ciphertext):', sha256(ciphertext))
    print('hash(d1) :', sha256(d1))
    print('hash(d2) :', sha256(d2))

def stress_test():
    print('_'*30)
    print('stress test:')
    for i in range(50):
        key = os.urandom(8)
        cipher = DES(key, 'CBC')
        data = os.urandom(i * 7 + 1)
        if cipher.decrypt(cipher.encrypt(data)) != data:
            print('failed')
            return
    print('passed')
    
        
def main():
    test_mode('ECB')
    test_mode('CBC')
    stress_test()

if __name__ == '__main__':
    main()
from project_DES import DES
import time
import hashlib

def sha256(data: str) -> bytes:
    return hashlib.sha256(data.encode()).digest()

def encrypt(key: str, plaintext: str, m: str) -> str:
    """encrypts a plaintext string using a string key and returns a hex string."""
    c = DES(sha256(key)[:8], mode = m)
    return c.encrypt(plaintext.encode()).hex()
    
def decrypt(key: str, ciphertext: str, m: str) -> str:
    """decrypts a ciphertext string using a string key and returns a hex string."""
    c = DES(sha256(key)[:8], mode = m)
    return c.decrypt(bytes.fromhex(ciphertext)).decode()

def main():
    ed = input('encrypt or decrypt? (e or d)')
    if ed == 'e':
        print('plaintext (blank line to end): ')
        p = []
        l = input()
        while l:
            p.append(l)
            l = input()
        p = '\n'.join(p)
        k = input('key: ')
        m = input('mode: ')
        print('_'*30, '\n')
        t = time.time()
        print(f'ciphertext (hex): \n{encrypt(k, p, m)}', '\n')
        print('time spent:', time.time()-t, 'sec')
    else:
        c = input('ciphertext (hex): ')
        k = input('key: ')
        m = input('mode: ')
        print('_'*30, '\n')
        t = time.time()
        print(f'plaintext: \n{decrypt(k, c, m)}', '\n')
        print('time spent:', time.time()-t,'sec')
        
if __name__ == "__main__":
    main()
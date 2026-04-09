from project_DES import DES
import time
import hashlib

def sha256(data: str) -> bytes:
    return hashlib.sha256(data.encode()).digest()

def encrypt(key: str, name: str, new_name: str, m: str):
    """encrypt a file using a string key and save it as 'new_name'."""
    c = DES(sha256(key)[:8], mode = m)
    c.encrypt_file(name, new_name)
    print(f'successfully encrypted {name} with {key} and saved it as {new_name}')
    
def decrypt(key: str, name: str, new_name: str, m: str):
    """decrypt a file using a string key and save it as 'new_name'."""
    c = DES(sha256(key)[:8], mode = m)
    c.decrypt_file(name, new_name)
    print(f'successfully decrypted {name} with {key} and saved it as {new_name}')

def main():
    ed = input('encrypt or decrypt? (e or d)')
    if ed == 'e':
        p = input('plaintext file name: ')
        n = input('name for encrypted file: ')
        k = input('key: ')
        m = input('mode: ')
        print('_'*30, '\n')
        t = time.time()
        encrypt(k, p, n, m)
        print('\ntime spent:', round(time.time()-t, 2),'sec') 
    else:
        c = input('ciphertext file name: ')
        n = input('name for decrypted file: ')
        k = input('key: ')
        m = input('mode: ')
        print('_'*30, '\n')
        t = time.time()
        decrypt(k, c, n, m)
        print('\ntime spent:', round(time.time()-t, 2),'sec')
        
if __name__ == "__main__":
    main()
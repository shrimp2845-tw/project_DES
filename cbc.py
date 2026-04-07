from des import DES
import block_utils as b
import file_utils as f

def xor(b1: bytes, b2: bytes):
    return bytes(i^j for i, j in zip(b1, b2))
    
def cbc_encrypt(file: str, new_name: str, key: str, iv: str):
    key = f.read_bytes(key, 8)
    iv = f.read_bytes(iv, 8)
    cipher = DES(key)
    data = f.read_bytes(file)
    blocks = b.split_file(b.add_padding(data), 8)
    c_bytes = b''
    v = iv
    for i in blocks:
        v = cipher.encrypt(xor(i, v))
        c_bytes += v
    f.write_bytes(new_name, c_bytes)

def cbc_decrypt(file: str, new_name: str, key: str, iv: str):
    key = f.read_bytes(key, 8)
    iv = f.read_bytes(iv, 8)
    cipher = DES(key)
    data = f.read_bytes(file)
    blocks = b.split_file(data, 8)
    va = [iv] + blocks[:-1]
    p_bytes = b''.join(xor(cipher.decrypt(i), j) for i, j in zip(blocks, va))
    p_bytes = b.remove_padding(p_bytes)
    f.write_bytes(new_name, p_bytes)

def main():
    f = input('file name:')
    iv = input('initialization vector:')
    k = input('key name:')
    n = input('new name:')
    ed = input('encrypt or decrypt? (e or d)')
    if ed == 'e':
        cbc_encrypt(f, n, k, iv)
    else:
        cbc_decrypt(f, n, k, iv)

if __name__ == "__main__":
    main()
    
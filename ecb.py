from des import DES
import block_utils as b
import file_utils as f

def ecb_encrypt(file: str, new_name: str, key: str):
    key = f.read_bytes(key, 8)
    cipher = DES(key)
    data = f.read_bytes(file)
    blocks = b.split_file(b.add_padding(data), 8)
    c_bytes = b''.join(cipher.encrypt(i) for i in blocks)
    f.write_bytes(new_name, c_bytes)

def ecb_decrypt(file: str, new_name: str, key: str):
    key = f.read_bytes(key, 8)
    cipher = DES(key)
    data = f.read_bytes(file)
    blocks = b.split_file(data, 8)
    p_bytes = b''.join(cipher.decrypt(i) for i in blocks)
    p_bytes = b.remove_padding(p_bytes)
    f.write_bytes(new_name, p_bytes)

def main():
    f = input('file name:')
    k = input('key name:')
    n = input('new name:')
    ed = input('encrypt or decrypt? (e or d)')
    if ed == 'e':
        ecb_encrypt(f, n, k)
    else:
        ecb_decrypt(f, n, k)

if __name__ == "__main__":
    main()

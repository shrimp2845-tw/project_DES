from des import DES
import block_utils as b

def read_bytes(key: str, l: int):
    bfile = open(key, 'rb')
    data = bfile.read()
    bfile.close()
    if len(data) < l:
        raise ValueError('read_bytes: index overflow')
    return data[:l]
    
def ecb_encrypt(file: str, new_name: str, key: str):
    key = read_bytes(key, 8)
    cipher = DES(key)
    bfile = open(file, 'rb')
    data = bfile.read()
    bfile.close()
    blocks = b.split_file(b.add_padding(data), 8)
    c_bytes = b''
    for i in blocks:
        c_bytes += cipher.encrypt(i)
    o_file = open(new_name, 'wb')
    o_file.write(c_bytes)
    o_file.close()

def ecb_decrypt(file: str, new_name: str, key: str):
    key = read_bytes(key, 8)
    cipher = DES(key)
    bfile = open(file, 'rb')
    data = bfile.read()
    bfile.close()
    blocks = b.split_file(data, 8)
    p_bytes = b''
    for i in blocks:
        p_bytes += cipher.decrypt(i)
    p_bytes = b.remove_padding(p_bytes)
    o_file = open(new_name, 'wb')
    o_file.write(p_bytes)
    o_file.close()

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

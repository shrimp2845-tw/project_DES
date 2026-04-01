from des import DES
import block_utils as b
import os

def ecb_encrypt(file: str, key: bytes):
    cipher = DES(key)
    bfile = open(file, 'rb')
    data = bfile.read()
    bfile.close()
    blocks = b.split_file(b.add_padding(data), 8)
    c_bytes = b''
    for i in blocks:
        c_bytes += cipher.encrypt(i)
    o_file = open(f'{os.path.splitext(file)[0]}.bin', 'wb')
    o_file.write(c_bytes)
    o_file.close()

def ecb_decrypt(file: str, extension: str, key: bytes):
    cipher = DES(key)
    bfile = open(file, 'rb')
    data = bfile.read()
    bfile.close()
    blocks = b.split_file(data, 8)
    p_bytes = b''
    for i in blocks:
        p_bytes += cipher.decrypt(i)
    o_file = open(f'{os.path.splitext(file)[0]}_decrypted.{extension}', 'wb')
    o_file.write(p_bytes)
    o_file.close()

def main():
    pass

if __name__ == "__main__":
    main()

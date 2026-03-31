from des import DES
import block_utils as b
import os

def ebc_encrypt(file: str, key: bytes):
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

def ebc_decrypt(file: str, extension: str, key: bytes):
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
    #ebc_encrypt("hina.png", b'M\xde\xab\xb9s\\\x12\x11')
    #ebc_decrypt("hina.bin", 'png', b'M\xde\xab\xb9s\\\x12\x11')
    #ebc_encrypt("mumei.jpg", b'\x1c\xb3*\x88"vu\x1f')
    ebc_decrypt("mumei.bin", "jpg" ,b'\x1c\xb3*\x88"vu\x1f')


if __name__ == "__main__":
    main()
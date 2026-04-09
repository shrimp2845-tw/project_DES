from .des_core import BasicDES
from typing import Union, Iterable
import os

def read_bytes(name: str, l = 0) -> bytes:
    """read bytes from target file"""
    bfile = open(name, 'rb')
    data = bfile.read()
    bfile.close()
    if l == 0:
        return data
    return data[:l]
    
def write_bytes(name: str, data: bytes):
    """write bytes into a new created file"""
    bfile = open(name, 'wb')
    bfile.write(data)
    bfile.close()
    
class DES:
    def __init__(self, key: Union[bytes, str], mode: str = 'ECB'):
        """setting initial mode and cipher machine"""
        self.modes = {'ECB', 'CBC'}
        if isinstance(key, str):
            key = read_bytes(key, 8)
        if len(key) != 8:
            raise ValueError('DES: invalid key')
        self.cipher = BasicDES(key)
        self.__key = key
        if mode not in self.modes:
            raise ValueError('DES: unknown mode of operation')
        self.__mode = mode
            
    @staticmethod
    def __add_padding(file: bytes) -> bytes:
        """add padding to a bytes string"""
        if not isinstance(file, bytes):
            raise TypeError
        if len(file)%8 == 0:
            return file + b'\x08'*8
        return file + bytes([8-(len(file)%8)]*(8-(len(file)%8)))

    @staticmethod
    def __remove_padding(file: bytes) -> bytes:
        """remove padding from a bytes string"""
        if not isinstance(file, bytes):
            raise TypeError
        pl = file[-1]
        if pl > 8 or pl < 1 or file[-pl:] != bytes([pl])*pl:
            return file
        return file[:-pl]
        
    @staticmethod
    def __split_data(file: bytes) -> list[bytes]:
        """split a bytes string to a list contain bytes strings with length of 8"""
        if (len(file)%8) != 0:
            raise ValueError ('split_data: data must be splited perfectly')
        return [file[i: i+8] for i in range(0, len(file), 8)]
    
    @staticmethod
    def __merge_data(blocks: Iterable[bytes]) -> bytes:
        """merge a list contain bytes strings into bytes string"""
        return b''.join(blocks)
        
    @staticmethod
    def __random_iv() -> bytes:
        """generate a random initialization vector for cbc encryption"""
        return os.urandom(8)
        
    @staticmethod
    def __xor(b1: bytes, b2: bytes):
        """perform xor operation between two bytes string of equal length"""
        return bytes(i^j for i, j in zip(b1, b2))
    
    def __ecb(self, blocks: list[bytes], decrypt: bool = False) -> bytes:
        """perform encrypt & decryption of ECB method"""
        if not decrypt:
            return self.__merge_data(self.cipher.encrypt(i) for i in blocks)
        else:
            return self.__remove_padding(self.__merge_data(self.cipher.decrypt(i) for i in blocks))
    
    def __cbc(self, blocks: list[bytes], decrypt: bool = False) -> bytes:
        """perform encryption & decryption of CBC method"""
        if not decrypt:
            v = self.__random_iv()
            cipher_data = [v] 
            for i in blocks:
                v = self.cipher.encrypt(self.__xor(i, v))
                cipher_data.append(v)
            return self.__merge_data(cipher_data)
        else:
            if len(blocks) < 2:
                raise ValueError("cbc: ciphertext too short")
            va, blocks = blocks[:-1], blocks[1:]
            return self.__remove_padding(self.__merge_data(self.__xor(self.cipher.decrypt(i), j) for i, j in zip(blocks, va)))
              
    def get_modes(self) -> list[str]:
        """get avaliable cipher mode of operation"""
        return self.modes
        
    def get_mode(self) -> str:
        """get current cipher mode of operation"""
        return self.__mode
    
    def change_mode(self, mode: str):
        """change current cipher mode of operation"""
        if mode not in self.modes:
            raise ValueError('change_mode: unknown mode of operation')
        self.__mode = mode
     
    def get_key(self) -> bytes:
        """get current using key"""
        return self.__key      
       
    def change_key(self, key: Union[bytes, str]):
        """change current using key"""
        if isinstance(key, str):
            key = read_bytes(key, 8)
        if len(key) != 8:
            raise ValueError('change_key: invalid key')
        self.cipher = BasicDES(key)
        self.__key = key
        
    def encrypt(self, plaintext: bytes) -> bytes:
        """encrypt bytes data"""
        blocks = self.__split_data(self.__add_padding(plaintext))
        mode = self.__mode
        if mode == 'ECB':
            return self.__ecb(blocks)
        elif mode == 'CBC':
            return self.__cbc(blocks)
             
    def decrypt(self, ciphertext: bytes) -> bytes:
        """decrypt bytes data"""
        blocks = self.__split_data(ciphertext)
        mode = self.__mode
        if mode == 'ECB':
            return self.__ecb(blocks, decrypt = True)
        elif mode == 'CBC':
            return self.__cbc(blocks, decrypt = True)
            
    def encrypt_file(self, name: str, new_name: str):
        """encrypt target file and save it as 'new_name' """
        plaintext = read_bytes(name)
        ciphertext = self.encrypt(plaintext)
        write_bytes(new_name, ciphertext)
    
    def decrypt_file(self, name: str, new_name: str):
        """decrypt target file and save it as 'new_name' """
        ciphertext = read_bytes(name)
        plaintext = self.decrypt(ciphertext)
        write_bytes(new_name, plaintext)
                
def main():
    pass

if __name__ == "__main__":
    main()

**_Warning: This implementation is intended for self learning purposes only and should not be used for real-world security._**

## About

- **Author:** shrimp2845  
- **Version:** 0.1.0  
- **License:** MIT

This is an educational Python implementation of the Data Encryption Standard (DES). This project breaks down the complex Feistel network into human-readable modules following the official NIST specifications, and supports ECB and CBC modes for real file encryption.

## Installation & Usage

### install
Requires Python 3.10+
```bash
pip install project-des
```
### usage
```bash
python -c "from project_DES import DES; cipher = DES(b'12345678'); print(cipher.encrypt(b'data').hex())"
```

## Docs

```
class initialize
----------------------
project_DES.DES(key, mode='ECB')

key 
-> 8 bytes or key file name 
containing an encryption key,
if key is str, it extract 
first 8 bytes in the file

mode
-> optional, block cipher mode of 
operation that used,ECB and CBC 
available in current version


methods
----------------------

encrypt(data: bytes) -> bytes, 
decrypt(data: bytes) -> bytes
-> return encrypt/decrypt bytes data

encrypt_file(name: str, new_name: str), 
decrypt_file(name: str, new_name: str) 
-> encrypt/decrypt target file 'name' 
and save it as 'new_name'

get_key(), get_mode()
-> get current using key/mode of 
operation

change_key(key: str or bytes),
change_mode(mode: str)
-> change current using key/mode of 
operation

```

## Examples
Project provides two examples: [string_cipher.py](https://github.com/shrimp2845-tw/project_DES/blob/main/examples/string_cipher.py) & [file_cipher.py](https://github.com/shrimp2845-tw/project_DES/blob/main/examples/file_cipher.py)

you can find samples of [file_cipher.py](https://github.com/shrimp2845-tw/project_DES/blob/main/examples/file_cipher.py) at:
[ecb_sample](https://github.com/shrimp2845-tw/project_DES/tree/main/examples/ecb_sample) & [cbc_sample](https://github.com/shrimp2845-tw/project_DES/tree/main/examples/cbc_sample)

### explanation for samples
**mumei.jpg**: plaintext file

**mumei.bin**: encrypt mumei.jpg with key ‘berries’ and mode ECB

**mumei_correct_decrypt**.jpg: decrypt mumei.bin with key ‘berries’ and mode ECB

**mumei_wrong_decrypt.jpg**: decrypt  mumei.bin with key ‘friend’ and mode ECB

**ina.jpg**: plaintext file 

**ina.bin**: encrypt ina.jpg with key ‘takodachi’ and mode CBC

**ina_correct_decrypt.jpg**: decrypt ina.bin with key ‘takodachi’ and mode CBC

**ina_wrong_decrypt.jpg**: decrypt ina.bin with key ‘violet’ and mode CBC


## Performance 
This project is designed for learning and understanding how DES works  rather than for practical encryption use. The implementation prioritizes readability and modular structure over performance.

As a result, encryption process is **very slow**. It takes nearly 2 minutes to encrypt 1MB file.





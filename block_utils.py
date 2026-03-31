def add_padding(file: bytes):
    if type(file) != bytes:
        raise TypeError
    if len(file)%8 == 0:
        return file + b'\x08'*8
    return file + int.to_bytes(8-(len(file)%8))*(8-len(file)%8)

def remove_padding(file: bytes):
    if type(file) != bytes:
        raise TypeError
    pl = file[-1]
    return file[:-pl]

def split_file(file: bytes, size: int):
    return [file[i: i+size] for i in range(0, len(file), size)]

def merge_file(blocks: list[bytes]):
    return b''.join(blocks)

def main():
    pass

if __name__ == "__main__":
    main()
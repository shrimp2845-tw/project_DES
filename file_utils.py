def read_bytes(name: str, l = 0):
    bfile = open(name, 'rb')
    data = bfile.read()
    bfile.close()
    if l == 0:
        return data
    return data[:l]
    
def write_bytes(name: str, data: bytes):
    bfile = open(name, 'wb')
    bfile.write(data)
    bfile.close()
    
def main():
    pass

if __name__ == "__main__":
    main()
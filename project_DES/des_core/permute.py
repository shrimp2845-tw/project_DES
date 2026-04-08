
meticulous_mode = True

def permutation(btd: list[int], table: list[int])  -> list[int]:
    if meticulous_mode and len(btd) < max(table):
        raise ValueError('permutation:index overflow')
    n_btd = [btd[i-1] for i in table]
    return n_btd

def main():
    pass
    
if __name__ == "__main__":
    main()

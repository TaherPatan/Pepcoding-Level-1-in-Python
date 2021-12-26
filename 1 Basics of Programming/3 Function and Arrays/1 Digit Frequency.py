if __name__ == '__main__':
    n = input()
    d = str(int(input()))
    freq = 0
    for i in n:
        if i == d:
            freq += 1
    print(int(freq))

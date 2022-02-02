def find_base(num, base):
    num_base = 0
    i = 0
    while num > 0:
        if i == 0:
            num_base = num % base
        else:
            num_base += (num % base) * 10 ** i
        num = num // base
        i += 1
    return num_base


if __name__ == '__main__':
    n = int(input())
    base = int(input())
    print(find_base(n, base))

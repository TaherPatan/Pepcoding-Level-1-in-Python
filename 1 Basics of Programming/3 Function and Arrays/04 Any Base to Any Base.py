def find_dec(num, base):
    return int(num, base)


def dec_to_base(num, base):
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
    n = input()
    b1 = int(input())
    b2 = int(input())
    dec = find_dec(n, b1)
    print(dec_to_base(dec, b2))

def find_num(num, base):
    return int(num, base)


if __name__ == '__main__':
    n = input()
    b = int(input())
    print(find_num(n, b))

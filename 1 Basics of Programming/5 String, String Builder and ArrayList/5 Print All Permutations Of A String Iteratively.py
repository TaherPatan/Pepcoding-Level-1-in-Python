def factorial(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x


def printallperm(st):
    for i in range(factorial(len(st))):
        lst = list(st)
        mul = i
        for j in range(len(st), 0, -1):
            rem = mul % j
            mul = mul // j
            print(lst.pop(rem), end='')
        print()


if __name__ == '__main__':
    st = input()
    printallperm(st)

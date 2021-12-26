def printIncDec(n):
    if n == 0:
        return
    print(n)
    printIncDec(n - 1)
    print(n)


if __name__ == '__main__':
    n = int(input())
    printIncDec(n)

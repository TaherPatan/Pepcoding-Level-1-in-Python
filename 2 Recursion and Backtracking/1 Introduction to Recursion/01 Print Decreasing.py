def printDecreasing(n):
    if n == 1:
        print(1)
        return
    print(n)
    printDecreasing(n - 1)


if __name__ == '__main__':
    n = int(input())
    printDecreasing(n)

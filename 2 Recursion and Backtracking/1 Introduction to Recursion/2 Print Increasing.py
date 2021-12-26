def printIncreasing(n):
    if n == 0:
        return
    printIncreasing(n - 1)
    print(n)


if __name__ == '__main__':
    n = int(input())
    printIncreasing(n)

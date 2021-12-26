def printZigZag(n):
    if n == 0:
        return
    print(n, end=' ')
    printZigZag(n - 1)
    print(n, end=' ')
    printZigZag(n - 1)
    print(n, end=' ')


if __name__ == "__main__":
    num = int(input())
    printZigZag(num)

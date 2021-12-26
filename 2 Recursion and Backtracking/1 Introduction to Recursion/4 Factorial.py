def factorial(x):
    if x == 2:
        return 2
    return x * factorial(x - 1)


if __name__ == "__main__":
    num = int(input())
    print(factorial(num))

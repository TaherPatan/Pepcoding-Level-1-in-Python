def powerLinear(x, n):
    if n == 0:
        return 1
    return x * powerLinear(x, n - 1)


if __name__ == "__main__":
    num = int(input())
    power = int(input())
    print(powerLinear(num, power))

import sys
sys.setrecursionlimit(1500)

def powerLog(x, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return (xpn := powerLog(x, n // 2)) * xpn * x
    return (xpn := powerLog(x, n // 2)) * xpn


if __name__ == "__main__":
    num = int(input())
    power = int(input())
    print(powerLog(num, power))

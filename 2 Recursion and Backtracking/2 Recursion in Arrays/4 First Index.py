import sys
sys.setrecursionlimit(3000)


def Firstindex(arr, idx, x, n):
    if idx == n:
        print(-1)
        return
    elif arr[idx] == x:
        print(idx)
        return
    Firstindex(arr, idx + 1, x, n)


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    x = int(input())
    Firstindex(arr, 0, x, n)

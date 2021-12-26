import sys

sys.setrecursionlimit(10000)


def max(arr, idx, n):
    if idx == n - 1:
        return arr[idx]
    res = max(arr, idx + 1, n)
    if arr[idx] > res:
        return arr[idx]
    else:
        return res


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    res = max(arr, 0, n)
    print(res)

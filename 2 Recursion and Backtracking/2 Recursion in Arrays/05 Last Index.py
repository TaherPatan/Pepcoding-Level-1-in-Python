import sys
sys.setrecursionlimit(3000)


def Lastindex(arr, idx, x):
    if idx == -1:
        return - 1
    elif arr[idx] == x:
        return idx
    return Lastindex(arr, idx - 1, x)


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    x = int(input())
    print(Lastindex(arr, n - 1, x))

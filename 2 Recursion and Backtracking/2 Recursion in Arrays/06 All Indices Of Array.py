import sys
sys.setrecursionlimit(10000)


def find_indices(arr, idx, x, fsf):
    if idx == len(arr):
        return [0] * fsf
    if arr[idx] == x:
        fsf += 1
    lst = find_indices(arr, idx + 1, x, fsf)
    if arr[idx] == x:
        lst[fsf - 1] = idx
    return lst


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    x = int(input())
    lst = find_indices(arr, 0, x, 0)
    for i in lst:
        print(i)

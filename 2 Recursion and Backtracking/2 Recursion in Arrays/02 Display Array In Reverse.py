def displayinrev(arr, idx, n):
    if idx == n:
        return
    displayinrev(arr, idx + 1, n)
    print(arr[idx])


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    displayinrev(arr, 0, n)

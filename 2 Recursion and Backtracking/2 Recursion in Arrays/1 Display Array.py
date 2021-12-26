def display(arr, idx, n):
    if idx == n:
        return
    print(arr[idx])
    display(arr, idx + 1, n)


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    display(arr, 0, n)

def Display(arr):
    for i in arr:
        print(i, end=" ")


def countsort(arr, d):
    freq = [0] * 10
    for i in range(0, len(arr)):
        idx = (arr[i] // d) % 10
        freq[idx] += 1
    for i in range(1, len(freq)):
        freq[i] = freq[i] + freq[i - 1]
    ans = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        idx = (arr[i] // d) % 10
        ans[freq[idx] - 1] = arr[i]
        freq[idx] -= 1
    for i in range(0, len(arr)):
        arr[i] = ans[i]
    print(f'After sorting on {d} place ->', end=' ')
    Display(arr)
    print()


def radixSort(arr):
    max_val = max(arr)
    exp = 1
    while exp <= max_val:
        countsort(arr, exp)
        exp *= 10


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    radixSort(arr)
    Display(arr)

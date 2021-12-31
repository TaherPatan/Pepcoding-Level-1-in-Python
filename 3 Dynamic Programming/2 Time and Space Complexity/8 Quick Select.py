def swap(arr, i, j):
    print(f'Swapping {arr[i]} and {arr[j]}')
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, pivot, lo, hi):
    print(f'pivot -> {pivot}')
    prev = lo - 1
    for curr in range(lo, hi + 1):
        if arr[curr] <= pivot:
            prev = prev + 1
            swap(arr, curr, prev)
    print(f'pivot index -> {prev}')
    return prev


def quickselect(arr, lo, hi, k):
    if hi < lo:
        return
    piv_idx = partition(arr, arr[hi], lo, hi)
    if piv_idx == k:
        return arr[piv_idx]
    elif k < piv_idx:
        return quickselect(arr, lo, piv_idx - 1, k)
    elif piv_idx < k:
        return quickselect(arr, piv_idx + 1, hi, k)


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    k = int(input())
    ans = quickselect(arr, 0, n - 1, k - 1)
    print(ans)

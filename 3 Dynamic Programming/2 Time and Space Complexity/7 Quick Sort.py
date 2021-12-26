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
    print("pivot index ->", prev)
    return prev


def quicksort(arr, lo, hi):
    if hi < lo:
        return
    piv_idx = partition(arr,arr[hi], lo, hi)
    quicksort(arr, lo, piv_idx - 1)
    quicksort(arr, piv_idx + 1, hi)


def Display(arr):
    for i in range(0, len(arr)) :
        print(arr[i], end=' ')


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    quicksort(arr, 0, n - 1)
    Display(arr)

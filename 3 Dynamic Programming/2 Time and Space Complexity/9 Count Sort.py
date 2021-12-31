def count_sort(arr, max_val, min_val):
    freq_arr_size = max_val - min_val + 1
    freq = [0] * freq_arr_size
    for i in range(0, len(arr)):
        idx = arr[i] - min_val
        freq[idx] += 1
    for i in range(1, len(freq)):
        freq[i] += freq[i - 1]
    ans = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        idx = arr[i] - min_val
        ans[freq[idx] - 1] = arr[i]
        freq[idx] -= 1
    for i in range(0, len(arr)):
        arr[i] = ans[i]


def Display(arr):
    for i in range(0, len(arr)):
        print(arr[i])


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    min_val = min(arr)
    max_val = max(arr)
    count_sort(arr, max_val, min_val)
    Display(arr)

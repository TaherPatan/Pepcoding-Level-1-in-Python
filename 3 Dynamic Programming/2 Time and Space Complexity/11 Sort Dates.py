def Display(arr):
    for i in arr:
        if len(str(i)) == 8:
            print(i)
        else:
            print(f'0{i}')


def count_sort(arr, d, mod, r):
    freq_arr = [0] * r
    for i in range(len(arr)):
        freq_arr[((arr[i] // d) % mod)] += 1
    for i in range(1, len(freq_arr)):
        freq_arr[i] += freq_arr[i - 1]
    ans = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        idx = (arr[i] // d) % mod
        ans[freq_arr[idx] - 1] = arr[i]
        freq_arr[idx] -= 1
    for i in range(len(arr)):
        arr[i] = ans[i]


def sort_dates(arr):
    count_sort(arr, 1000000, 100, 32)
    count_sort(arr, 10000, 100, 13)
    count_sort(arr, 1, 10000, 2501)


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    sort_dates(arr)
    Display(arr)

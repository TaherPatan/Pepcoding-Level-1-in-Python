def swap(arr, i, j):
    print("Swapping index", i, "and index", j);
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def Display(arr):
    for i in arr:
        print(i)


def sort01(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            swap(arr, i, j)
            j += 1


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    sort01(arr)
    Display(arr)

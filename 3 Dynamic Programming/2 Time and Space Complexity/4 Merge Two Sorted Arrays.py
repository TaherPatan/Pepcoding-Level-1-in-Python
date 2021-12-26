def mergeArrays(arr1, arr2, n1, n2):
    i = j = k = 0
    lst = [0] * (n1 + n2)
    while j < n1 and k < n2:
        if arr1[j] <= arr2[k]:
            lst[i] = arr1[j]
            j += 1
            i += 1
        else:
            lst[i] = arr2[k]
            i += 1
            k += 1
    if j < n1:
        while j < n1:
            lst[i] = arr1[j]
            i += 1
            j += 1
    elif k < n2:
        while k < n1:
            lst[i] = arr2[k]
            i += 1
            k += 1
    for i in lst:
        print(i)


if __name__ == '__main__':
    n = int(input())
    arr1 = [int(input()) for _ in range(n)]
    m = int(input())
    arr2 = [int(input()) for _ in range(m)]
    mergeArrays(arr1, arr2, n, m)

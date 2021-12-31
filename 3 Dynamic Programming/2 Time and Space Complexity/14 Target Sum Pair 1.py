def targetSumPair(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] < target:
            i += 1
        elif target < arr[i] + arr[j]:
            j -= 1
        elif arr[i] + arr[j] == target:
            print(f'{arr[i]}, {arr[j]}')
            i += 1
            j -= 1


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    target = int(input())
    targetSumPair(arr, target)

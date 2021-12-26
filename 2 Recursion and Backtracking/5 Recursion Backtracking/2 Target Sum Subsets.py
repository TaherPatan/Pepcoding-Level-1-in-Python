def printTargetSumSubsets(arr, idx, asf, sos, tar):
    if sos > tar:
        return
    if idx == len(arr):
        if sos == tar:
            print(asf + '.')
        return
    printTargetSumSubsets(arr, idx + 1, f"{asf}{arr[idx]}, ", sos + arr[idx], tar)
    printTargetSumSubsets(arr, idx + 1, asf, sos, tar)


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    tar = int(input())
    printTargetSumSubsets(arr, 0, '', 0, tar)

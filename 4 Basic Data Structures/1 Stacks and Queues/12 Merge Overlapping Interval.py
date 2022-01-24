def mergeOverlappingIntervals(lst):
    stack = [lst.pop(0)]
    for ele in lst:
        if stack[-1][0] <= ele[0] <= stack[-1][1]:
            stack[-1][1] = max(stack[-1][1], ele[1])
        else:
            stack.append(ele)
    return stack


if __name__ == '__main__':
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort()
    lst = mergeOverlappingIntervals(lst)
    for ele in lst:
        print(f'{ele[0]} {ele[1]}')
def find_greater_element(arr):
    stack = []
    ans = []
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    ans = find_greater_element(arr)
    for i in range(len(arr) - 1, -1, -1):
        print(ans[i])

def stock_span(arr):
    stack = []
    ans = []
    for i in range(len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            ans.append(i - stack[-1])
        else:
            ans.append(i + 1)
        stack.append(i)
    return ans


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    ans = stock_span(arr)
    for i in ans:
        print(i)
